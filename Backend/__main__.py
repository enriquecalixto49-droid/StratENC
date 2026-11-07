"""
Entry point:  python -m <your_package> [--source fred equity fx crypto]
                                        [--category us_rates us_credit ...]
                                        [--start 2015-01-01] [--skip-static]

1. Syncs the static dicts into the static tables (tk, name, category).
2. Reads the tickers back from each static table (optionally filtered by category).
3. Passes them to the existing uploaders, which fill the time series tables.
"""
import argparse
import asyncio

from sqlalchemy import text

from .uploaders.macro import FredUploader
from .session import SessionLocal, engine
from .static_data.static_repo import StaticUploader  
from .static_data.static_repo import STATIC_TABLES  
from .uploaders.tiingo import get_uploader
from .tables import macroS, equityS, FXS, cryptoS  


SOURCES = {
    "fred":   macroS,
    "equity": equityS,
    "fx":     FXS,
    "crypto": cryptoS,
}


async def sync_static(source: str) -> None:
    """
    Dict -> static table (upsert).
    """
    table = SOURCES[source]
    repo = StaticUploader(table)
    await repo.save(repo.to_records(STATIC_TABLES[table]))


async def read_static(source: str, categories: list[str] | None) -> dict[str, str]:
    """
    Static table -> {tk: name}.
    """
    query = f"SELECT tk, name FROM {SOURCES[source]}"
    params: dict = {}
    if categories:
        query += " WHERE category = ANY(:cats)"
        params["cats"] = categories
    async with SessionLocal() as session:
        result = await session.execute(text(query + " ORDER BY tk"), params)
        return {tk: name for tk, name in result}


async def run_source(source: str, categories: list[str] | None, start: str | None) -> None:
    universe = await read_static(source, categories)
    if not universe:
        print(f"== {source}: no tickers (check --category) ==")
        return
    tickers = list(universe)
    print(f"== {source}: {len(tickers)} tickers ==")

    if source == "fred":
        await FredUploader().upload_many(tickers, names=universe)
    else:
        await get_uploader(source, static_data=universe).upload_many(tickers, start)


async def main() -> None:
    '''
    Set up the shell command line interface and run the appropriate data uploaders based on user input.
    Example usage:
        python -m Backend --source fred equity --category us_rates us_credit --start 2015-01-01
        python -m Backend # sync static tables + load everything
        python -m Backend --source fred --category us_rates us_credit
        python -m Backend --source equity crypto --start 2024-01-01 --skip-static
    '''
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--source", nargs="+", choices=list(SOURCES)) # python app.py --source fred tiingo
    ap.add_argument("--category", nargs="+")
    ap.add_argument("--start", help="start date for Tiingo downloads (FRED always downloads full history)")
    # by default we sync the static tables, but this option allows you to skip that step if you know the static data is already up to date
    ap.add_argument("--skip-static", action="store_true", help="do not re-sync the static tables") 
    args = ap.parse_args()

    try:
        for source in args.source or list(SOURCES):
            try:
                if not args.skip_static:
                    await sync_static(source)
                await run_source(source, args.category, args.start)
            except Exception as e:  # one broken source must not stop the others
                print(f"[{source}] aborted: {e!r}")
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
TIINGO_FX_REDUCED = {

    "g10_majors": {
        "eurusd": "EUR / USD", "gbpusd": "GBP / USD", "usdjpy": "USD / JPY",
        "usdchf": "USD / CHF", "usdcad": "USD / CAD", "audusd": "AUD / USD",
        "nzdusd": "NZD / USD",
    }
}

# ----------------------------------------------------------------------
# TIINGO_FX_SERIES: 28 pairs (was 56). 1 API request per pair.
# Removed: the commodity_crosses bucket and the least liquid / most redundant crosses.
# ----------------------------------------------------------------------
TIINGO_FX_SERIES = {

    "g10_majors": {  # 7
        "eurusd": "EUR / USD", "gbpusd": "GBP / USD", "usdjpy": "USD / JPY",
        "usdchf": "USD / CHF", "usdcad": "USD / CAD", "audusd": "AUD / USD",
        "nzdusd": "NZD / USD",
    },

    "eur_crosses": {  # 4
        "eurgbp": "EUR / GBP", "eurchf": "EUR / CHF", "eurjpy": "EUR / JPY",
        "euraud": "EUR / AUD",
    },

    "gbp_crosses": {  # 2
        "gbpjpy": "GBP / JPY", "gbpchf": "GBP / CHF",
    },

    "jpy_crosses": {  # 2
        "audjpy": "AUD / JPY", "chfjpy": "CHF / JPY",
    },

    "scandinavia": {  # 2
        "usdsek": "USD / SEK", "usdnok": "USD / NOK",
    },

    "cee_emea": {  # 4
        "usdpln": "USD / PLN", "usdhuf": "USD / HUF",
        "usdtry": "USD / TRY", "usdzar": "USD / ZAR",
    },

    "asia": {  # 4
        "usdcnh": "USD / CNH (offshore yuan)", "usdsgd": "USD / SGD",
        "usdinr": "USD / INR", "usdkrw": "USD / KRW",
    },

    "latam": {  # 3
        "usdmxn": "USD / MXN", "usdbrl": "USD / BRL", "usdclp": "USD / CLP",
    }
}

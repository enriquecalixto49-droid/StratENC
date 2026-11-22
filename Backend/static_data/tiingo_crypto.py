TIINGO_CRYPTO_REDUCED = {

    "large_cap": {
        "btcusd": "Bitcoin / USD", "ethusd": "Ethereum / USD", "bnbusd": "BNB / USD",
        "xrpusd": "XRP / USD", "solusd": "Solana / USD", "adausd": "Cardano / USD",
        "dogeusd": "Dogecoin / USD", "trxusd": "TRON / USD",
    }
}

# ----------------------------------------------------------------------
# TIINGO_CRYPTO_SERIES: 26 pairs (was 48). 1 API request per pair.
# maticusd was dropped on purpose: Polygon migrated MATIC -> POL in 2024, so that
# ticker may return no data. Check Tiingo's supported list before adding it back.
# ----------------------------------------------------------------------
TIINGO_CRYPTO_SERIES = {

    "large_cap": {  # 8
        "btcusd": "Bitcoin / USD", "ethusd": "Ethereum / USD", "bnbusd": "BNB / USD",
        "xrpusd": "XRP / USD", "solusd": "Solana / USD", "adausd": "Cardano / USD",
        "dogeusd": "Dogecoin / USD", "trxusd": "TRON / USD",
    },

    "layer1": {  # 4
        "avaxusd": "Avalanche / USD", "dotusd": "Polkadot / USD", "atomusd": "Cosmos / USD",
        "nearusd": "NEAR Protocol / USD",
    },

    "layer2_scaling": {  # 2
        "arbusd": "Arbitrum / USD", "opusd": "Optimism / USD",
    },

    "defi": {  # 3
        "uniusd": "Uniswap / USD", "aaveusd": "Aave / USD", "ldousd": "Lido DAO / USD",
    },

    "infrastructure_oracle": {  # 1
        "linkusd": "Chainlink / USD",
    },

    "payments_legacy_privacy": {  # 3
        "ltcusd": "Litecoin / USD", "bchusd": "Bitcoin Cash / USD", "xlmusd": "Stellar / USD",
    },

    "meme": {  # 2
        "shibusd": "Shiba Inu / USD", "pepeusd": "Pepe / USD",
    },

    "stablecoins": {  # 2
        "usdtusd": "Tether / USD", "usdcusd": "USD Coin / USD",
    },

    "crypto_crosses": {  # 1
        "ethbtc": "Ethereum / Bitcoin",
    }
}

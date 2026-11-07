TIINGO_EQUITY_REDUCED = {

    "us_broad_etf": {
        "SPY": "SPDR S&P 500 ETF Trust",
        "QQQ": "Invesco QQQ Trust (Nasdaq 100)",
        "IWM": "iShares Russell 2000 ETF"
    },

    "us_style_etf": {
        "IWD": "iShares Russell 1000 Value ETF",
        "IWF": "iShares Russell 1000 Growth ETF",
        "QUAL": "iShares MSCI USA Quality Factor ETF"
    },

    "us_sector_etf": {
        "XLE": "Energy Select Sector SPDR",
        "XLF": "Financial Select Sector SPDR",
        "XLV": "Health Care Select Sector SPDR",
        "XLI": "Industrial Select Sector SPDR",
        "XLRE": "Real Estate Select Sector SPDR",
        "XLK": "Technology Select Sector SPDR",
    },

    "intl_etf": {
        "EFA": "iShares MSCI EAFE ETF",
        "EEM": "iShares MSCI Emerging Markets ETF",
        "VGK": "Vanguard FTSE Europe ETF",
        "FEZ": "SPDR EURO STOXX 50 ETF",
        "EWJ": "iShares MSCI Japan ETF",
        "FXI": "iShares China Large-Cap ETF",
        "INDA": "iShares MSCI India ETF",
        "EWZ": "iShares MSCI Brazil ETF",
    },

    "fixed_income_etf": {
        "SHY": "iShares 1-3 Year Treasury Bond ETF",
        "IEF": "iShares 7-10 Year Treasury Bond ETF",
        "TLT": "iShares 20+ Year Treasury Bond ETF",
        "TIP": "iShares TIPS Bond ETF",
        "AGG": "iShares Core U.S. Aggregate Bond ETF",
        "LQD": "iShares iBoxx Investment Grade Corporate Bond ETF",
        "HYG": "iShares iBoxx High Yield Corporate Bond ETF",
        "EMB": "iShares J.P. Morgan USD Emerging Markets Bond ETF",
    },

    "commodity_etf": {
        "GLD": "SPDR Gold Shares",
        "SLV": "iShares Silver Trust",
        "USO": "United States Oil Fund",
        "UNG": "United States Natural Gas Fund",
        "DBC": "Invesco DB Commodity Index Tracking Fund",
        "DBA": "Invesco DB Agriculture Fund",
        "CPER": "United States Copper Index Fund",
    }
}

# We can add more categories in the future, but for now, we will focus on these ETFs for simplicity and to avoid hitting Tiingo's free account request limit.

TIINGO_EQUITY_SERIES = {

    "us_broad_etf": {
        "SPY": "SPDR S&P 500 ETF Trust",
        "VOO": "Vanguard S&P 500 ETF",
        "IVV": "iShares Core S&P 500 ETF",
        "VTI": "Vanguard Total Stock Market ETF",
        "QQQ": "Invesco QQQ Trust (Nasdaq 100)",
        "DIA": "SPDR Dow Jones Industrial Average ETF",
        "IWM": "iShares Russell 2000 ETF",
        "MDY": "SPDR S&P MidCap 400 ETF",
    },

    "us_style_etf": {
        "IWD": "iShares Russell 1000 Value ETF",
        "IWF": "iShares Russell 1000 Growth ETF",
        "MTUM": "iShares MSCI USA Momentum Factor ETF",
        "QUAL": "iShares MSCI USA Quality Factor ETF",
        "USMV": "iShares MSCI USA Min Vol Factor ETF",
        "VLUE": "iShares MSCI USA Value Factor ETF",
    },

    "us_sector_etf": {
        "XLC": "Communication Services Select Sector SPDR",
        "XLY": "Consumer Discretionary Select Sector SPDR",
        "XLP": "Consumer Staples Select Sector SPDR",
        "XLE": "Energy Select Sector SPDR",
        "XLF": "Financial Select Sector SPDR",
        "XLV": "Health Care Select Sector SPDR",
        "XLI": "Industrial Select Sector SPDR",
        "XLB": "Materials Select Sector SPDR",
        "XLRE": "Real Estate Select Sector SPDR",
        "XLK": "Technology Select Sector SPDR",
        "XLU": "Utilities Select Sector SPDR",
    },

    "us_industry_etf": {
        "SMH": "VanEck Semiconductor ETF",
        "KRE": "SPDR S&P Regional Banking ETF",
        "XBI": "SPDR S&P Biotech ETF",
        "XOP": "SPDR S&P Oil & Gas Exploration & Production ETF",
        "OIH": "VanEck Oil Services ETF",
        "ITA": "iShares U.S. Aerospace & Defense ETF",
    },

    "intl_etf": {
        "EFA": "iShares MSCI EAFE ETF",
        "EEM": "iShares MSCI Emerging Markets ETF",
        "VGK": "Vanguard FTSE Europe ETF",
        "FEZ": "SPDR EURO STOXX 50 ETF",
        "EWG": "iShares MSCI Germany ETF",
        "EWU": "iShares MSCI United Kingdom ETF",
        "EWQ": "iShares MSCI France ETF",
        "EWL": "iShares MSCI Switzerland ETF",
        "EWJ": "iShares MSCI Japan ETF",
        "FXI": "iShares China Large-Cap ETF",
        "INDA": "iShares MSCI India ETF",
        "EWZ": "iShares MSCI Brazil ETF",
    },

    "fixed_income_etf": {
        "SHY": "iShares 1-3 Year Treasury Bond ETF",
        "IEF": "iShares 7-10 Year Treasury Bond ETF",
        "TLT": "iShares 20+ Year Treasury Bond ETF",
        "TIP": "iShares TIPS Bond ETF",
        "AGG": "iShares Core U.S. Aggregate Bond ETF",
        "LQD": "iShares iBoxx Investment Grade Corporate Bond ETF",
        "HYG": "iShares iBoxx High Yield Corporate Bond ETF",
        "JNK": "SPDR Bloomberg High Yield Bond ETF",
        "EMB": "iShares J.P. Morgan USD Emerging Markets Bond ETF",
        "MUB": "iShares National Muni Bond ETF",
    },

    "commodity_etf": {
        "GLD": "SPDR Gold Shares",
        "SLV": "iShares Silver Trust",
        "USO": "United States Oil Fund",
        "UNG": "United States Natural Gas Fund",
        "DBC": "Invesco DB Commodity Index Tracking Fund",
        "DBA": "Invesco DB Agriculture Fund",
        "CPER": "United States Copper Index Fund",
    },

    "currency_etf": {
        "UUP": "Invesco DB US Dollar Index Bullish Fund",
        "FXE": "Invesco CurrencyShares Euro Trust",
        "FXY": "Invesco CurrencyShares Japanese Yen Trust",
        "FXF": "Invesco CurrencyShares Swiss Franc Trust",
    },

    "tech": {
        "AAPL": "Apple Inc.", "MSFT": "Microsoft Corp.", "NVDA": "NVIDIA Corp.",
        "AVGO": "Broadcom Inc.", "ORCL": "Oracle Corp.", "AMD": "Advanced Micro Devices Inc.",
        "CRM": "Salesforce Inc.", "ADBE": "Adobe Inc.", "CSCO": "Cisco Systems Inc.",
        "INTC": "Intel Corp.", "QCOM": "Qualcomm Inc.", "TXN": "Texas Instruments Inc.",
        "IBM": "International Business Machines Corp.", "NOW": "ServiceNow Inc.",
        "INTU": "Intuit Inc.", "MU": "Micron Technology Inc.", "AMAT": "Applied Materials Inc.",
        "LRCX": "Lam Research Corp.", "KLAC": "KLA Corp.", "PANW": "Palo Alto Networks Inc.",
        "PLTR": "Palantir Technologies Inc.", "ANET": "Arista Networks Inc.",
    },

    "communication": {
        "GOOGL": "Alphabet Inc. Class A", "META": "Meta Platforms Inc.",
        "NFLX": "Netflix Inc.", "DIS": "Walt Disney Co.", "T": "AT&T Inc.",
        "VZ": "Verizon Communications Inc.", "TMUS": "T-Mobile US Inc.",
        "CMCSA": "Comcast Corp.", "CHTR": "Charter Communications Inc.",
    },

    "consumer_discretionary": {
        "AMZN": "Amazon.com Inc.", "TSLA": "Tesla Inc.", "HD": "Home Depot Inc.",
        "MCD": "McDonald's Corp.", "LOW": "Lowe's Companies Inc.", "NKE": "Nike Inc.",
        "SBUX": "Starbucks Corp.", "BKNG": "Booking Holdings Inc.", "TJX": "TJX Companies Inc.",
        "GM": "General Motors Co.", "F": "Ford Motor Co.", "ABNB": "Airbnb Inc.",
        "CMG": "Chipotle Mexican Grill Inc.", "MAR": "Marriott International Inc.",
    },

    "consumer_staples": {
        "WMT": "Walmart Inc.", "PG": "Procter & Gamble Co.", "KO": "Coca-Cola Co.",
        "COST": "Costco Wholesale Corp.", "PEP": "PepsiCo Inc.", "PM": "Philip Morris International Inc.",
        "MO": "Altria Group Inc.", "MDLZ": "Mondelez International Inc.", "CL": "Colgate-Palmolive Co.",
        "KMB": "Kimberly-Clark Corp.", "TGT": "Target Corp.", "GIS": "General Mills Inc.",
        "KHC": "Kraft Heinz Co.",
    },

    "health_care": {
        "LLY": "Eli Lilly and Co.", "UNH": "UnitedHealth Group Inc.", "JNJ": "Johnson & Johnson",
        "MRK": "Merck & Co. Inc.", "ABBV": "AbbVie Inc.", "PFE": "Pfizer Inc.",
        "TMO": "Thermo Fisher Scientific Inc.", "ABT": "Abbott Laboratories", "AMGN": "Amgen Inc.",
        "GILD": "Gilead Sciences Inc.", "ISRG": "Intuitive Surgical Inc.", "MDT": "Medtronic plc",
        "BMY": "Bristol-Myers Squibb Co.", "DHR": "Danaher Corp.", "CVS": "CVS Health Corp.",
        "REGN": "Regeneron Pharmaceuticals Inc.", "VRTX": "Vertex Pharmaceuticals Inc.",
    },

    "financials": {
        "JPM": "JPMorgan Chase & Co.", "BAC": "Bank of America Corp.", "GS": "Goldman Sachs Group Inc.",
        "MS": "Morgan Stanley", "BRK-B": "Berkshire Hathaway Inc. Class B", "V": "Visa Inc.",
        "MA": "Mastercard Inc.", "WFC": "Wells Fargo & Co.", "C": "Citigroup Inc.",
        "SCHW": "Charles Schwab Corp.", "BLK": "BlackRock Inc.", "AXP": "American Express Co.",
        "SPGI": "S&P Global Inc.", "MMC": "Marsh & McLennan Companies Inc.",
        "PGR": "Progressive Corp.", "CB": "Chubb Ltd.", "BX": "Blackstone Inc.", "USB": "U.S. Bancorp",
    },

    "energy_upstream_services": {
        "XOM": "Exxon Mobil Corp.", "CVX": "Chevron Corp.", "COP": "ConocoPhillips",
        "EOG": "EOG Resources Inc.", "OXY": "Occidental Petroleum Corp.", "DVN": "Devon Energy Corp.",
        "FANG": "Diamondback Energy Inc.", "SLB": "Schlumberger Ltd.", "HAL": "Halliburton Co.",
        "BKR": "Baker Hughes Co.",
    },

    "energy_midstream_refining": {
        "KMI": "Kinder Morgan Inc.", "WMB": "Williams Companies Inc.", "OKE": "ONEOK Inc.",
        "ET": "Energy Transfer LP", "EPD": "Enterprise Products Partners LP",
        "LNG": "Cheniere Energy Inc.", "MPC": "Marathon Petroleum Corp.",
        "VLO": "Valero Energy Corp.", "PSX": "Phillips 66",
    },

    "industrials": {
        "CAT": "Caterpillar Inc.", "GE": "GE Aerospace", "GEV": "GE Vernova Inc.",
        "HON": "Honeywell International Inc.", "RTX": "RTX Corp.", "LMT": "Lockheed Martin Corp.",
        "NOC": "Northrop Grumman Corp.", "GD": "General Dynamics Corp.", "BA": "Boeing Co.",
        "DE": "Deere & Co.", "UPS": "United Parcel Service Inc.", "UNP": "Union Pacific Corp.",
        "CSX": "CSX Corp.", "ETN": "Eaton Corp. plc", "EMR": "Emerson Electric Co.",
        "ITW": "Illinois Tool Works Inc.", "MMM": "3M Co.", "WM": "Waste Management Inc.",
        "FDX": "FedEx Corp.", "LHX": "L3Harris Technologies Inc.",
    },

    "materials": {
        "LIN": "Linde plc", "SHW": "Sherwin-Williams Co.", "APD": "Air Products and Chemicals Inc.",
        "ECL": "Ecolab Inc.", "DD": "DuPont de Nemours Inc.", "DOW": "Dow Inc.",
        "NUE": "Nucor Corp.", "STLD": "Steel Dynamics Inc.", "FCX": "Freeport-McMoRan Inc.",
        "NEM": "Newmont Corp.", "SCCO": "Southern Copper Corp.",
    },

    "agriculture": {
        "ADM": "Archer-Daniels-Midland Co.", "BG": "Bunge Global SA",
        "CTVA": "Corteva Inc.", "MOS": "Mosaic Co.",
    },

    "utilities": {
        "NEE": "NextEra Energy Inc.", "DUK": "Duke Energy Corp.", "SO": "Southern Co.",
        "D": "Dominion Energy Inc.", "AEP": "American Electric Power Co.", "SRE": "Sempra",
        "EXC": "Exelon Corp.", "XEL": "Xcel Energy Inc.", "PCG": "PG&E Corp.",
        "CEG": "Constellation Energy Corp.", "VST": "Vistra Corp.",
    },

    "real_estate": {
        "PLD": "Prologis Inc.", "AMT": "American Tower Corp.", "EQIX": "Equinix Inc.",
        "CCI": "Crown Castle Inc.", "PSA": "Public Storage", "O": "Realty Income Corp.",
        "SPG": "Simon Property Group Inc.", "WELL": "Welltower Inc.", "DLR": "Digital Realty Trust Inc.",
    },

    "adr": {
        "TSM": "Taiwan Semiconductor Manufacturing Co. ADR", "ASML": "ASML Holding NV ADR",
        "NVO": "Novo Nordisk A/S ADR", "NVS": "Novartis AG ADR", "UBS": "UBS Group AG",
        "SAP": "SAP SE ADR", "SHEL": "Shell plc ADR", "BP": "BP plc ADR",
        "TTE": "TotalEnergies SE ADR", "TM": "Toyota Motor Corp. ADR",
        "BABA": "Alibaba Group Holding Ltd. ADR", "DEO": "Diageo plc ADR",
    }
}
FRED_MACRO_SERIES = {

    # ============ UNITED STATES ============

    "us_growth": {
        "GDPC1": "US Real GDP",
        "GDP": "US Nominal GDP",
        "INDPRO": "US Industrial Production Index",
        "PAYEMS": "US Nonfarm Payrolls",
        "RRSFS": "US Real Retail Sales",
        "RSAFS": "US Retail Sales",
        "UMCSENT": "University of Michigan Consumer Sentiment",
    },

    "us_labor": {
        "UNRATE": "US Unemployment Rate",
        "U6RATE": "US U6 Unemployment Rate",
        "ICSA": "US Initial Jobless Claims",
        "JTSJOL": "US JOLTS Job Openings",
        "CE16OV": "US Civilian Employment",
    },

    "us_inflation": {
        "CPIAUCSL": "US CPI All Urban Consumers",
        "CPILFESL": "US Core CPI",
        "PCEPI": "US PCE Price Index",
        "PCEPILFE": "US Core PCE Price Index",
        "PPIACO": "US Producer Price Index",
        "T5YIE": "US 5Y Breakeven Inflation",
        "T10YIE": "US 10Y Breakeven Inflation",
    },

    "us_rates": {
        "FEDFUNDS": "Effective Fed Funds Rate",
        "DGS1MO": "US Treasury 1M Yield",
        "DGS3MO": "US Treasury 3M Yield",
        "DGS2": "US Treasury 2Y Yield",
        "DGS5": "US Treasury 5Y Yield",
        "DGS10": "US Treasury 10Y Yield",
        "DGS30": "US Treasury 30Y Yield",
        "T10Y2Y": "US 10Y minus 2Y Treasury Spread",
        "T10Y3M": "US 10Y minus 3M Treasury Spread",
    },

    "us_credit": {
        "AAA": "AAA Corporate Bond Yield",
        "BAA": "BAA Corporate Bond Yield",
        "BAA10Y": "BAA minus 10Y Treasury Spread",
        "BAMLH0A0HYM2": "US High Yield OAS",
        "NFCI": "Chicago Fed National Financial Conditions Index",
        "ANFCI": "Chicago Fed Adjusted National Financial Conditions Index",
        "STLFSI4": "St. Louis Fed Financial Stress Index",
    },

    "us_liquidity": {
        "M1SL": "US M1 Money Supply",
        "M2SL": "US M2 Money Supply",
        "BOGMBASE": "US Monetary Base",
        "WALCL": "Federal Reserve Total Assets",
    },

    "us_housing": {
        "CSUSHPISA": "Case-Shiller US National House Price Index",
        "HOUST": "Housing Starts",
        "PERMIT": "Building Permits",
        "EXHOSLUSM495S": "Existing Home Sales",
    },

    "us_external": {
        "BOPGSTB": "US Trade Balance",
        "DTWEXBGS": "Trade Weighted US Dollar Index",
    },

    "us_markets": {
        "SP500": "S&P 500 Index",
        "VIXCLS": "VIX Volatility Index",
        "DCOILWTICO": "WTI Crude Oil Spot Price",
        "GOLDAMGBD228NLBM": "Gold Price London Bullion Market",
    },

    # ============ EURO AREA ============

    "euro_growth": {
        "CLVMNACSCAB1GQEA19": "Euro Area Real GDP",
        "PRINTO01EZM661N": "Euro Area Industrial Production",
        "EA19PRCNTO01GYSAM": "Euro Area Retail Sales Growth",
    },

    "euro_labor": {
        "LRHUTTTTEZM156S": "Euro Area Harmonised Unemployment Rate",
        "LRUNTTTTEZM156S": "Euro Area Unemployment Rate (OECD)",
    },

    "euro_inflation": {
        "CP0000EZ19M086NEST": "Euro Area HICP Inflation",
        "CPHPLTT01EZM659N": "Euro Area Core HICP",
        "CPALTT01EZM657N": "Euro Area CPI YoY",
    },

    "euro_money_supply": {
        "MYAGM1EZM189N": "Euro Area M1",
        "MYAGM2EZM196N": "Euro Area M2",
        "MYAGM3EZM196N": "Euro Area M3",
    },

    "euro_external": {
        "DEXUSEU": "USD per EUR Exchange Rate",
    },

    "euro_govt_debt": {
        "IRLTLT01DEM156N": "Germany 10Y Government Bond Yield",
        "IRLTLT01ITM156N": "Italy 10Y Government Bond Yield",
        "IRLTLT01FRM156N": "France 10Y Government Bond Yield",
        "IRLTLT01ESM156N": "Spain 10Y Government Bond Yield",
    },

    # ============ GLOBAL / OECD ============

    "global_oecd": {
        "LORSGPNO": "OECD Leading Indicator (GDP, normalised)",
    }
}
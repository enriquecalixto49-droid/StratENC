# <StratENC>

A web app for daily market research and simple strategy backtesting.

![Python](https://img.shields.io/badge/Python-backend-blue.svg)
![C++](https://img.shields.io/badge/C%2B%2B-backtest%20engine-00599C.svg)
![React](https://img.shields.io/badge/React-frontend-61DAFB.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)

## Overview

The project has two parts:

1. **Research Corner:** indicators retrieved and updated daily from market and macroeconomic data sources, presented in a clean dashboard.
2. **Strategy Lab:** a section where simple strategies can be configured and backtested against historical data. The backtest runs in a C++ engine for speed.

## Features

### Research Corner
- Daily data ingestion from Tiingo (prices) and FRED (macroeconomic series)
- Precomputed indicators (moving averages, momentum, volatility, macro spreads, etc.)
- Charts and tables for browsing series and indicators

### Strategy Lab
- Parameterized built-in strategies (e.g. SMA crossover, momentum, mean reversion, buy and hold)
- Configurable transaction costs and slippage
- Results: equity curve, trade list, and performance metrics (CAGR, volatility, Sharpe ratio, max drawdown, turnover)

> Feature lists describe the target scope. See the [Roadmap](#roadmap) for current status.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend / API | Python |
| Backtest engine | C++ (exposed to Python) |
| Database | PostgreSQL |
| Data sources | Tiingo, FRED (options and futures: to be defined, possibly Polygon) |

## Architecture

```
Tiingo / FRED ──► Python ingestion (daily job) ──► Database
                                                      │
React ◄──────────── Python API ◄──────────────────────┤
                        │                             │
                        └──► C++ backtest engine ◄────┘
```

- **Ingestion:** a scheduled job fetches new data daily and stores it in the database.
- **Indicators:** computed after ingestion and stored, so the frontend never calls external APIs directly.
- **API:** serves indicators and series to the frontend and launches backtests.
- **Engine:** takes price data plus a strategy and its parameters, and returns the equity curve, trades, and metrics.

## Project Structure

```
.
├── backend/      # API, ingestion jobs, data models
├── engine/       # C++ backtest engine and Python bindings
├── frontend/     # React app
├── docs/
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- A C++17 compiler and CMake 3.15+
- PostgreSQL
- API keys for [Tiingo](https://www.tiingo.com/) and [FRED](https://fred.stlouisfed.org/docs/api/api_key.html)

### Configuration

Create a `.env` file in `backend/`:

```env
TIINGO_API_KEY=your_key
FRED_API_KEY=your_key

DB_HOST=localhost
DB_PORT=5432
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
```

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Engine

```bash
cd engine
mkdir build && cd build
cmake ..
cmake --build . --config Release
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Backtesting Methodology

- Signals are generated at the close of day *t* and executed at day *t+1* to avoid look-ahead bias.
- Prices are adjusted for splits and dividends.
- Transaction costs and slippage are configurable parameters.
- Results are historical simulations and do not guarantee future performance.

## Data Sources and Licensing

| Source | Used for |
|---|---|
| [Tiingo](https://www.tiingo.com/) | Equity and ETF prices |
| [FRED](https://fred.stlouisfed.org/) | Macroeconomic series |
| Options / futures | To be defined (possibly [Polygon](https://polygon.io/)) |

Check each provider's terms of use before redistributing raw data publicly.

## Roadmap

- [ ] Ingestion pipeline for Tiingo and FRED into the database
- [ ] Daily indicator computation
- [ ] Research Corner: charts and tables
- [ ] C++ engine: first strategy and metrics
- [ ] Python bindings and `/backtest` endpoint
- [ ] Strategy Lab UI: parameter form and results page
- [ ] Additional strategies
- [ ] Options and futures data support
- [ ] Tests and CI

## Disclaimer

This project is for educational and research purposes only and is not financial advice.


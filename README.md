# 📈 Stock Viewer App (Finnhub API)
A simple Python CLI app that fetches real-time stock data using the Finnhub API.

## Features
- Real-life quotes
- Company information
- Secure API key handling using '.env'

## Technologies
- Python
- Requests
- Finmhub API
- python-dotenv

## Setup

1. Clone the repo
```bash
git clone https://github.com/Divnoorheer/stock_viewer
cd stock_project
```

2. Create virtual environment (usually preferred)
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
python -m pip install finnhub-python python-dotenv
```

4. Create .env
In order to get your api key, please register yourself on "https://finnhub.io/"
```bash
FINNHUB_API_KEY=your_api_key_here
```

5. Run the app
```bash
python stock.py
```


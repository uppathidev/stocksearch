from flask import Flask, jsonify
import yfinance as yf
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/stock/summary/<symbol>')
def get_stock_summary(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return jsonify({
            "previousClose": info.get('previousClose'),
            "open": info.get('open'),
            "bid": info.get('bid'),
            "ask": info.get('ask'),
            "daysRange": f"{info.get('dayLow', 'N/A')} - {info.get('dayHigh', 'N/A')}",
            "52WeekRange": f"{info.get('fiftyTwoWeekLow', 'N/A')} - {info.get('fiftyTwoWeekHigh', 'N/A')}",
            "volume": info.get('volume'),
            "avgVolume": info.get('averageVolume'),
            "marketCap": info.get('marketCap'),
            "beta": info.get('beta'),
            "peRatio": info.get('trailingPE'),
            "eps": info.get('trailingEps'),
            "earningsDate": info.get('earningsDate'),
            "dividendYield": info.get('dividendYield'),
            "targetEstimate": info.get('targetMeanPrice')
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/historical/<symbol>/<timeframe>')
def get_historical_data(symbol, timeframe):
    try:
        period_map = {
            '1D': '1d', '1W': '5d', '1M': '1mo',
            '3M': '3mo', '1YR': '1y', '3YR': '3y',
            '5YR': '5y', 'ALL': 'max'
        }
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period_map.get(timeframe, '1y'), interval='1d')
        return jsonify(hist.reset_index().to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/news/<symbol>')
def get_stock_news(symbol):
    try:
        stock = yf.Ticker(symbol)
        news = stock.news

        # Check if news is empty
        if not news:
            return jsonify({"error": "No news available for the given stock."}), 404

        return jsonify(news)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/financials/<symbol>')
def get_financials(symbol):
    try:
        stock = yf.Ticker(symbol)
        return jsonify({
            "income_stmt": stock.income_stmt.to_dict(),
            "balance_sheet": stock.balance_sheet.to_dict(),
            "cash_flow": stock.cashflow.to_dict()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/holdings/<symbol>')
def get_holdings(symbol):
    try:
        stock = yf.Ticker(symbol)
        return jsonify({
            "institutional_holders": stock.institutional_holders.to_dict(),
            "major_holders": stock.major_holders.to_dict()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/analysis/<symbol>')
def get_analysis(symbol):
    try:
        stock = yf.Ticker(symbol)

        # Convert recommendations and earnings_dates to dictionaries with string keys
        recommendations = stock.recommendations.reset_index().to_dict(orient='records')
        earnings_estimates = stock.earnings_dates.reset_index().to_dict(orient='records')

        return jsonify({
            "recommendations": recommendations,
            "earnings_estimates": earnings_estimates
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/stock/peers/<symbol>')
def get_peers(symbol):
    try:
        api_key = 'd0ounq9r01qr8ds0dhvgd0ounq9r01qr8ds0di00'
        url = f'https://finnhub.io/api/v1/stock/peers?symbol={symbol}&token={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            peers = response.json()
            # Remove the symbol itself from the list
            peers = [peer for peer in peers if peer != symbol.upper()]
            return jsonify({"peers": peers})
        else:
            return jsonify({"error": "Failed to fetch peers"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/dividends/<symbol>')
def get_dividends(symbol):
    try:
        stock = yf.Ticker(symbol)
        dividends = stock.dividends.reset_index().to_dict(orient='records')
        return jsonify(dividends)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/stock/earnings/<symbol>')
def get_earnings(symbol):
    try:
        stock = yf.Ticker(symbol)
        earnings = stock.earnings_dates.reset_index().to_dict(orient='records')
        return jsonify(earnings)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/splits/<symbol>')
def get_splits(symbol):
    try:
        stock = yf.Ticker(symbol)
        splits = stock.splits.reset_index().to_dict(orient='records')
        return jsonify(splits)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/sustainability/<symbol>')
def get_sustainability(symbol):
    try:
        stock = yf.Ticker(symbol)
        sustainability = stock.sustainability.to_dict()
        return jsonify(sustainability)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/options/<symbol>')
def get_options(symbol):
    try:
        stock = yf.Ticker(symbol)
        expirations = stock.options
        options_chain = {}
        for date in expirations:
            options_chain[date] = {
                "calls": stock.option_chain(date).calls.to_dict(orient='records'),
                "puts": stock.option_chain(date).puts.to_dict(orient='records')
            }
        return jsonify(options_chain)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/insider/<symbol>')
def get_insider(symbol):
    try:
        stock = yf.Ticker(symbol)
        insider = stock.insider_transactions.reset_index().to_dict(orient='records')
        return jsonify(insider)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/stock/profile/<symbol>')
def get_profile(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        # Extract CEO name from companyOfficers
        ceo_name = None
        company_officers = info.get("companyOfficers", [])
        for officer in company_officers:
            if "title" in officer and "CEO" in officer["title"]:
                ceo_name = officer.get("name")
                break

        profile = {
            "longName": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "website": info.get("website"),
            "description": info.get("longBusinessSummary"),
            "ceo": ceo_name,
            "city": info.get("city"),
            "country": info.get("country"),
        }
        return jsonify(profile)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)

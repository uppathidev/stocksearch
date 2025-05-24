#### Stock API Project

This project provides a RESTful API for retrieving stock market data using the `yfinance` library. The API includes endpoints for fetching stock summaries, historical data, news, financials, and more.

---

### Features
- Retrieve stock summaries, historical prices, and news articles.
- Access financial statements, institutional holdings, and analyst recommendations.
- Fetch peer companies, dividend history, earnings calendar, and stock splits.
- Get ESG/Sustainability scores, options chain, insider transactions, and company profiles.

---

### Endpoints

| Endpoint                          | Method | Description                     | Parameters                     |
|-----------------------------------|--------|---------------------------------|--------------------------------|
| `/stock/summary/<symbol>`         | GET    | Get summary data                | `symbol`: Stock ticker         |
| `/stock/historical/<symbol>/<timeframe>` | GET | Historical prices              | `symbol`, `timeframe`: 1D,1W, etc. |
| `/stock/news/<symbol>`            | GET    | News articles                   | `symbol`                       |
| `/stock/financials/<symbol>`      | GET    | Financial statements            | `symbol`                       |
| `/stock/holdings/<symbol>`        | GET    | Institutional holdings          | `symbol`                       |
| `/stock/analysis/<symbol>`        | GET    | Analyst recommendations         | `symbol`                       |
| `/stock/peers/<symbol>`           | GET    | Peer companies                  | `symbol`                       |
| `/stock/dividends/<symbol>`       | GET    | Dividend history                | `symbol`                       |
| `/stock/earnings/<symbol>`        | GET    | Earnings calendar               | `symbol`                       |
| `/stock/splits/<symbol>`          | GET    | Stock splits history            | `symbol`                       |
| `/stock/sustainability/<symbol>`  | GET    | ESG/Sustainability scores       | `symbol`                       |
| `/stock/options/<symbol>`         | GET    | Options chain                   | `symbol`                       |
| `/stock/insider/<symbol>`         | GET    | Insider transactions            | `symbol`                       |
| `/stock/profile/<symbol>`         | GET    | Company profile/overview        | `symbol`                       |

---

### Getting Started

#### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)

#### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/stock-api-yahoo.git
   cd stock-api-yahoo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `yfinance` and `Flask` libraries are installed:
   ```bash
   pip install yfinance flask
   ```

---

### Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser or API testing tool (e.g., Postman) and access the API at:
   ```plaintext
   http://127.0.0.1:5000
   ```

---

### Example Usage

- **Get Stock Summary**:
  ```plaintext
  GET /stock/summary/AAPL
  ```

- **Get Historical Data**:
  ```plaintext
  GET /stock/historical/AAPL/1M
  ```

- **Get News Articles**:
  ```plaintext
  GET /stock/news/AAPL
  ```

---

### Contributing
Feel free to submit issues or pull requests to improve the project.

---

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
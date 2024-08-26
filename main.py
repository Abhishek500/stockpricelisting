from flask import Flask, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/get_stock_price', methods=['GET'])
def get_stock_price():
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Please provide a stock ticker"}), 400

    # Fetch the stock data from an API (example using Yahoo Finance API)
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}.NS?period1=0&period2=9999999999&interval=1d&events=history'
    try:
        data = pd.read_csv(url).head(200)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Convert the DataFrame to a dictionary and return it as JSON
    return jsonify(data.tail().to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

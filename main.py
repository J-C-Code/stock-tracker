# THIS API IS NOT FOR COMMERCIAL USE PER THE YFINANCE DOCS.
# THE CREATION AND PUBLICATION OF THIS PROJECT IS PURELY FOR 
# EDUCATIONAL PURPOSES


import yfinance as yf
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Stock-API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def history(self):
        tickName = yf.Ticker(self.ticker)
        hist = tickName.history(period="1mo")
        return hist.reset_index().to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
    
    def recommend(self):
        tickName = yf.Ticker(self.ticker)
        recommendation = tickName.recommendations
        return recommendation.reset_index().to_dict(orient='records')  # Convert DataFrame to a list of dictionaries

    def financials(self):
        tickName = yf.Ticker(self.ticker)
        finances = tickName.financials
        finances.reset_index(inplace=True)  # Reset index to avoid timestamp comparison issue
        finances.columns = finances.columns.astype(str)  # Convert column names to strings
        finances = finances.applymap(str)  # Convert all values to strings
        return finances.to_dict(orient='list')  # Convert DataFrame to dictionary with lists as values

    def info(self):
        tickName = yf.Ticker(self.ticker)
        info = tickName.info
        return info
    
    def cashflow(self):
        tickName = yf.Ticker(self.ticker)
        _cashFlow = tickName.cashflow
        _cashFlow.reset_index(inplace=True)
        _cashFlow.columns = _cashFlow.columns.astype(str)
        _cashFlow = _cashFlow.applymap(str)
        return _cashFlow.to_dict(orient='list')
    

@app.route('/history', methods=['GET'])
def stock_history():
    if request.method == 'GET':
        args = request.args
        if len(args) > 2:
            return jsonify({"error": "Request malformed: too many query parameters"}), 400
        if 'ticker' in args:
            ticker = args['ticker']
            ticker_instance = Ticker(ticker=str(ticker))
            history = ticker_instance.history()  # Call the method to get recommendations
            return jsonify(history)  # Return as JSON
        else:
            return jsonify({"error": "You must enter a stock ticker!"}), 400


@app.route('/cashflow', methods=['GET'])
def stock_cashflow():
    if request.method == 'GET':
        args = request.args
        if len(args) > 2:
            return jsonify({"error": "Request malformed: too many query parameters"}), 400
        if 'ticker' in args:
            ticker = args['ticker']
            ticker_instance = Ticker(ticker=str(ticker))
            _cashFlow = ticker_instance.cashflow()  # Call the method to get recommendations
            return jsonify(_cashFlow)  # Return as JSON
        else:
            return jsonify({"error": "You must enter a stock ticker!"}), 400


@app.route('/info', methods=['GET'])
def stock_info():
    if request.method == 'GET':
        args = request.args
        if len(args) > 2:
            return jsonify({"error": "Request malformed: too many query parameters"}), 400
        if 'ticker' in args:
            ticker = args['ticker']
            ticker_instance = Ticker(ticker=str(ticker))
            info = ticker_instance.info()  # Call the method to get recommendations
            return jsonify(info)  # Return as JSON
        else:
            return jsonify({"error": "You must enter a stock ticker!"}), 400



@app.route('/recommend', methods=['GET'])
def recommend_stock():
    if request.method == 'GET':
        args = request.args
        if len(args) > 2:
            return jsonify({"error": "Request malformed: too many query parameters"}), 400
        if 'ticker' in args:
            ticker = args['ticker']
            ticker_instance = Ticker(ticker=str(ticker))
            recommendation = ticker_instance.recommend()  # Call the method to get recommendations
            return jsonify(recommendation)  # Return as JSON
        else:
            return jsonify({"error": "You must enter a stock ticker!"}), 400


@app.route('/financials', methods=['GET'])
def price():
    if request.method == 'GET':
        args = request.args
        if len(args) > 2:
            return jsonify({"error": "Request malformed: too many query parameters"}), 400
        if 'ticker' in args:
            ticker = args['ticker']
            ticker_instance = Ticker(ticker=str(ticker))
            finances = ticker_instance.financials()  # Call the method to get recommendations
            return jsonify(finances)  # Return as JSON
        else:
            return jsonify({"error": "You must enter a stock ticker!"}), 400

if __name__ == '__main__': 
    app.run(debug=True)

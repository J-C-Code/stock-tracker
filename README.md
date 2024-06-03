# Stock Tracker API

## Local development

1. Create and activate Python virtual environment

    ```python
    python -m venv venv
    source venv/bin/activate # This works on Mac/Linux. Windows has another /bin/ file that is used to activate the Python virtual environment
    ```

2. Install requirements

    ```python
    pip install -r requirements.txt # This will install all required packages into your virtual environment
    ```

3. Now run your app!
   - Debug: Press `F5` or click the debug icon in your IDE
   - From terminal: Run `python main.py`

4. API can now be accessed from [http://localhost:5000/](http://localhost:5000/).
5. It is recommended for first-time users to check out swagger first, to do this start the program and go to [http://localhost:5000/swagger](http://localhost:5000/swagger).

## Endpoints

### `/history`

- **Method**: GET
- **Description**: Get historical data for a stock.
- **Parameters**:
  - `ticker`: Stock ticker symbol (required)
- **Response**:
  - Returns a list of historical data records including date, opening price, highest price, lowest price, closing price, trading volume, dividends, and stock splits.

### `/recommend`

- **Method**: GET
- **Description**: Get recommendations for a stock.
- **Parameters**:
  - `ticker`: Stock ticker symbol (required)
- **Response**:
  - Returns a list of recommendation records including date, recommending firm, assigned grade, previous grade, and recommended action.

### `/financials`

- **Method**: GET
- **Description**: Get financial information for a stock.
- **Parameters**:
  - `ticker`: Stock ticker symbol (required)
- **Response**:
  - Returns a list of financial records including date and various financial metrics.

### `/info`

- **Method**: GET
- **Description**: Get basic information for a stock.
- **Parameters**:
  - `ticker`: Stock ticker symbol (required)
- **Response**:
  - Returns a list of basic info regarding the company

## Disclaimer

This API is not for commercial use as per the Yahoo Finance API documentation. The creation and publication of this project are purely for educational purposes.

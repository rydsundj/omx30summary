import yfinance as yf
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    omx30_tickers = [
        "EVO.ST", "HM-B.ST", "VOLV-B.ST", "ERIC-B.ST", "SEB-A.ST",
        "ASSA-B.ST", "SHB-A.ST", "INVE-B.ST", "SWED-A.ST", "TELIA.ST",
        "NDA-SE.ST", "ESSITY-B.ST", "ALFA.ST", "SAAB-B.ST", "HEXA-B.ST",
        "TEL2-B.ST", "SCA-B.ST", "SKF-B.ST", "ELUX-B.ST", "SAND.ST",
        "ATCO-A.ST", "ATCO-B.ST", "SINCH.ST", "BOL.ST", "GETI-B.ST",
        "AZN.ST", "KINV-B.ST", "SBB-B.ST", "ABB.ST", "NIBE-B.ST"
    ]

    stock_data = {}

    for ticker in omx30_tickers:
        stock = yf.Ticker(ticker)
        try:
            forward_pe = stock.info.get("forwardPE", None)
            market_cap = stock.info.get("marketCap", None)
            stock_data[ticker] = {
                "pe": forward_pe,
                "market_cap": market_cap
            }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    sorted_stock_data = dict(
        sorted(stock_data.items(), key=lambda item: (item[1]["pe"] or float('inf')))
    )
    
    return jsonify(sorted_stock_data)

if __name__ == '__main__':
    app.run(debug=True)

import yfinance as yf
import json
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# List of OMX30 tickers

@app.route('/fetch-data', methods=['GET'])


def fetch_data():
    # Example: Fetch data for Apple stock
    omx30_tickers = [
    "EVO.ST", "HM-B.ST", "VOLV-B.ST", "ERIC-B.ST", "SEB-A.ST",
    "ASSA-B.ST", "SHB-A.ST", "INVE-B.ST", "SWED-A.ST", "TELIA.ST",
    "NDA-SE.ST", "ESSITY-B.ST", "ALFA.ST", "SAAB-B.ST", "HEXA-B.ST",
    "TEL2-B.ST", "SCA-B.ST", "SKF-B.ST", "ELUX-B.ST", "SAND.ST",
    "ATCO-A.ST", "ATCO-B.ST", "SINCH.ST", "BOL.ST", "GETI-B.ST",
    "AZN.ST", "KINV-B.ST", "SBB-B.ST", "ABB.ST", "NIBE-B.ST"
    ]

    pe_data = {}

    for ticker in omx30_tickers:
        stock = yf.Ticker(ticker)
        try:
            forward_pe = stock.info["forwardPE"]
            if forward_pe: 
                pe_data[ticker] = forward_pe
        except KeyError:
            print(f"Key 'forwardPE' not found for {ticker}.")
        
    sorted_pe_data = dict(sorted(pe_data.items(), key=lambda item: item[1]))
    return jsonify(sorted_pe_data)

if __name__ == '__main__':
    app.run(debug=True)

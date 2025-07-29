from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # ✅ מאפשר CORS כברירת מחדל

@app.route('/price')
def get_price():
    try:
        url = "https://api.dexscreener.com/latest/dex/pairs/ethereum/0x543a4ca897f901e5b14128f58b28c8d913471bc9"
        response = requests.get(url)
        data = response.json()
        pair_data = data.get("pair", {})

        return jsonify({
            "priceUsd": pair_data.get("priceUsd"),
            "marketCap": pair_data.get("fdv"),
            "liquidity": pair_data.get("liquidity", {}).get("usd"),
            "volume24h": pair_data.get("volume", {}).get("h24"),
            "txns": pair_data.get("txns", {})
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

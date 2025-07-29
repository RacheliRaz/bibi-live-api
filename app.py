from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/price')
def get_price():
    url = "https://api.dexscreener.com/latest/dex/pairs/ethereum/0xfA21cc13462fD156a2d11EB7b5c4812154C6f485"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"error": f"API returned status code {response.status_code}"}), 500

        data = response.json()
        if data is None or "pair" not in data:
            return jsonify({"error": "API response invalid or missing 'pair'"}), 500

        pair_data = data.get("pair", {})
        
        result = {
            "priceUsd": pair_data.get("priceUsd"),
            "marketCap": pair_data.get("fdv"),
            "liquidity": pair_data.get("liquidity", {}).get("usd"),
            "volume24h": pair_data.get("volume", {}).get("h24")
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

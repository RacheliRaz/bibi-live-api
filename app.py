from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/price')
def get_price():
    url = "https://api.dexscreener.com/latest/dex/pairs/ethereum/0x543a4ca897f901e5b14128f58b28c8d913471bc9"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({"error": f"API returned status code {response.status_code}"}), 500

        data = response.json()
        if data is None or not data.get("pair"):
            return jsonify({"error": "Pair not found or unavailable"}), 404

        pair_data = data["pair"]

        result = {
            "priceUsd": pair_data.get("priceUsd"),
            "marketCap": pair_data.get("fdv"),
            "liquidity": pair_data.get("liquidity", {}).get("usd"),
            "volume24h": pair_data.get("volume", {}).get("h24"),
            "txns": pair_data.get("txns", {}).get("h24"),
            "holders": pair_data.get("holders")  # אם יש כזה שדה – אם לא, תורידי
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

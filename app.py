from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API is live!"})

@app.route('/price')
def get_price():
    try:
        url = "https://api.dexscreener.com/latest/dex/pairs/ethereum/0x6Def1C8560552E589c3912391C4f5ed72c4625d4"
        response = requests.get(url)
        data = response.json().get('pair', {})

        return jsonify({
            "symbol": data.get("baseToken", {}).get("symbol", "N/A"),
            "price_usd": data.get("priceUsd", "N/A"),
            "volume_24h": data.get("volume", "N/A"),
            "liquidity_usd": data.get("liquidity", {}).get("usd", "N/A"),
            "market_cap": "N/A",  # נתון חסר ב-DexScreener
            "holders": "N/A",     # צריך למשוך מ-Etherscan
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

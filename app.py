from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API is live!"})

@app.route('/price')
def get_price():
    try:
        # מחלצים את נתוני המטבע מתוך DexScreener לפי הכתובת של הפול
        response = requests.get("https://api.dexscreener.com/latest/dex/pairs/ethereum/0x6Def1C8560552E589c3912391C4f5ed72c4625d4")
        data = response.json().get("pair", {})

        return jsonify({
            "symbol": data.get("baseToken", {}).get("symbol", "BIBI"),
            "price_usd": float(data.get("priceUsd", 0)),
            "volume_24h": float(data.get("volume", {}).get("h24", 0)),
            "liquidity_usd": float(data.get("liquidity", {}).get("usd", 0)),
            "market_cap_estimated": "N/A",  # שווי שוק לא תמיד זמין בדקססקרינר
            "tx_count_24h": data.get("txCount", {}).get("h24", 0),
            "holders": "N/A"  # DexScreener לא מספק מספר הולדרים
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

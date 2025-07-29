from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "API is live!"})

@app.route('/price')
def get_price():
    # דוגמה לנתון פיקטיבי – בהמשך נכניס נתונים אמיתיים
    return jsonify({
        "symbol": "BIBI",
        "price_usd": 0.00001234,
        "volume_24h": 18000,
        "holders": 928,
        "market_cap": 123456
    })

if __name__ == '__main__':
    app.run(debug=True)

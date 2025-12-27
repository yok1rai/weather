from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
import logging
import sys

# Suppress stdout/stderr temporarily
class DevNull:
    def write(self, msg): pass
    def flush(self): pass

sys.stdout = DevNull()
sys.stderr = DevNull()

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

app = Flask(__name__)

# Disable Flask/Werkzeug logs
logging.getLogger('werkzeug').disabled = True

# Restore stdout/stderr so your app can still print if needed
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY not found in .env file!")
API_KEY = API_KEY.strip()

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not specified"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 200 and data.get("cod") != "200":
            return jsonify({"error": data.get("message", "Unknown API error")}), 400

        return jsonify(data)

    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

if __name__ == "__main__":
    import logging
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True

    app.run(debug=False, host="127.0.0.1", port=5000)

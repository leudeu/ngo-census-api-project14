from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "NGO Census Data API is running"

@app.route("/census")
def census():
    return jsonify({
        "ngo": "Helping Hands NGO",
        "population_counted": 15423,
        "region": "North West Cameroon"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/api/user")
def get_user():
    return jsonify({
        "name": "Varshini",
        "referralCode": "varshini2025",
        "donationsRaised": 2500
    })

@app.route("/api/leaderboard")
def get_leaderboard():
    return jsonify([
        {"name": "Varshini", "amount": 2500},
        {"name": "Aarav", "amount": 1900},
        {"name": "Diya", "amount": 1700}
    ])

if __name__ == "__main__":
    app.run(debug=True)

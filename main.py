from flask import Flask, render_template

app = Flask(__name__)

cafes = [
    {"name": "Blue Bottle Cafe", "wifi": "Fast", "power": "Available", "location": "Downtown"},
    {"name": "Starbean Coffee", "wifi": "Good", "power": "Few outlets", "location": "Uptown"},
    {"name": "The Work Hub", "wifi": "Excellent", "power": "Plenty", "location": "Midtown"},
    {"name": "Cuppa Connect", "wifi": "Reliable", "power": "Available", "location": "East Side"}
]


@app.route("/")
def home():
    return render_template("index.html", cafes=cafes)   # 👈 pass cafes list


if __name__ == "__main__":
    app.run(debug=True)

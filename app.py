from flask import Flask, render_template, request, jsonify
import json
from rules import check_access

app = Flask(__name__)

@app.route("/")
def index():
    with open("employees.json") as f:
        employees = json.load(f)
    return render_template("index.html", employees=employees)

@app.route("/simulate", methods=["POST"])
def simulate():
    with open("employees.json") as f:
        employees = json.load(f)
    results = []
    for emp in employees:
        decision = check_access(emp)
        results.append({"id": emp["id"], "room": emp["room"], "result": decision})
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

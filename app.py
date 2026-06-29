from flask import Flask, jsonify, request
import math

app = Flask(__name__)


def compute_series(n_max: int):
    """Compute Big-O growth values for n = 1..n_max."""
    ns = list(range(1, n_max + 1))
    data = {
        "n": ns,
        "O(1)": [1 for _ in ns],
        "O(log n)": [math.log2(n) if n > 0 else 0 for n in ns],
        "O(n)": [n for n in ns],
        "O(n log n)": [n * math.log2(n) if n > 1 else 0 for n in ns],
        "O(n^2)": [n ** 2 for n in ns],
    }
    return data


@app.route("/")
def index():
    from flask import render_template
    return render_template("index.html")


@app.route("/api/complexity")
def complexity():
    try:
        n = int(request.args.get("n", 20))
    except ValueError:
        n = 20
    n = max(1, min(n, 100000))
    return jsonify(compute_series(n))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

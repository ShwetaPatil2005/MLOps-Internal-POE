from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = "MLOps UAT"
    if request.method == "POST":
        name = request.form.get("name", "").strip() or "MLOps UAT"
    return f"""
    <!doctype html>
    <html lang="en">
      <head><meta charset="utf-8"><title>MLOps UAT Hello</title></head>
      <body>
        <h1>Hello, {name}!</h1>
        <p>Simple Flask application for the MLOps Internal POE dry run.</p>
        <form method="post">
          <label for="name">Your name:</label>
          <input id="name" name="name" type="text">
          <button type="submit">Submit</button>
        </form>
        <p>Health check: <a href="/health">/health</a></p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

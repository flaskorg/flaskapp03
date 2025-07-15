from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Life can be unfair but we face it regardless",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency."
]

@app.route('/quote')
def quote():
    return random.choice(quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

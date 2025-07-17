from flask import Flask, render_template
import random

app = Flask(__name__)

funny_images = [
    "funny1.jpg",
    "funny2.jpg",
    "funny3.jpg",
    "funny4.jpg"
]

@app.route('/')
def home():
    selected_image = random.choice(funny_images)
    return render_template('funny.html', image=selected_image)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


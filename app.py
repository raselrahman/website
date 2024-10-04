from flask import Flask, render_template
import os  # Make sure to import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='A K Z Rasel Rahman')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

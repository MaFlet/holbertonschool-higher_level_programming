from flask import Flask, render_template
import json

app = Flask(__name__)

def read_items(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
            return data.get('items', [])
    except:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items = read_items('items.json')
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
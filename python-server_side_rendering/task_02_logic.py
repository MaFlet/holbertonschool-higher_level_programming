from flask import Flask, render_template
import json

app = Flask(__name__)

def read_json_file(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except:
        return {"items": []}

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
    data = read_json_file('items.json')
    items_list = data.get('items', ["Leanardo", "Python Book", "Flask Mug"])
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
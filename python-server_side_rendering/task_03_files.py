from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data(id=None):
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            if id is not None:
                filtered_data = [product for product in data if str(product.get('id')) == str(id)]
                if not filtered_data:
                    return None
                return filtered_data
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def load_csv_data(id=None):
    try:
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            for product in data:
                product['price'] = float(product['price'])
            if id is not None:
                filtered_data = [product for product in data if str(product.get('id')) == str(id)]
                if not filtered_data:
                    return None
                return filtered_data
            return data
    except FileNotFoundError:
        return []
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    items = []

    if source == 'json':
        items = load_json_data(product_id) or []
    elif source == 'csv':
        items = load_csv_data(product_id) or []

    error_message = "Wrong source" if source and source not in ['json', 'csv'] else None

    if items is None:
        error_message = "Product not found"
        items = []

    return render_template("product_display.html",
                           items=items,
                           error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
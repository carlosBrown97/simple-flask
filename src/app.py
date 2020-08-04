from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'response': 'Hello bitch!'})

# Get Data Routes
@app.route('/products')
def getProducts():
    return jsonify({'products': products})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()
    ]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
        return jsonify({'message': 'Product Not found'})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name
    ]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })

if __name__ == '__main__':
    app.run(debug=True, port=3000)

import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

carts = {}
orders = {}
items = {}

# Cart endpoints

# POST /cart
@app.route('/cart', methods=['POST'])
def create_cart():
    cart_id = generate_cart_id()
    carts[cart_id] = {}
    return jsonify({'cart_id': cart_id}), 201

# GET /cart/{cart_id}
@app.route('/cart/<cart_id>', methods=['GET'])
def get_cart(cart_id):
    if cart_id in carts:
        return jsonify(carts[cart_id])
    else:
        return jsonify({'error': 'Cart not found'}), 404

# PUT /cart/{cart_id}
@app.route('/cart/<cart_id>', methods=['PUT'])
def update_cart(cart_id):
    if cart_id in carts:
        carts[cart_id] = request.get_json()
        return jsonify({'message': 'Cart updated', 'cart_id': cart_id})
    else:
        return jsonify({'error': 'Cart not found'}), 404

# DELETE /cart/{cart_id}
@app.route('/cart/<cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    if cart_id in carts:
        del carts[cart_id]
        return jsonify({'message': 'Cart deleted', 'cart_id': cart_id})
    else:
        return jsonify({'error': 'Cart not found'}), 404

# Order endpoints

# POST /order
@app.route('/order', methods=['POST'])
def create_order():
    order_id = generate_order_id()
    orders[order_id] = {}
    return jsonify({'order_id': order_id}), 201

# GET /order/{order_id}
@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    if order_id in orders:
        return jsonify(orders[order_id])
    else:
        return jsonify({'error': 'Order not found'}), 404

# PUT /order/{order_id}
@app.route('/order/<order_id>', methods=['PUT'])
def update_order(order_id):
    if order_id in orders:
        orders[order_id] = request.get_json()
        return jsonify({'message': 'Order updated', 'order_id': order_id})
    else:
        return jsonify({'error': 'Order not found'}), 404

# DELETE /order/{order_id}
@app.route('/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    if order_id in orders:
        del orders[order_id]
        return jsonify({'message': 'Order deleted', 'order_id': order_id})
    else:
        return jsonify({'error': 'Order not found'}), 404

# Item endpoints

# POST /items
@app.route('/items', methods=['POST'])
def add_item():
    item_id = generate_item_id()
    items[item_id] = request.get_json()
    return jsonify({'item_id': item_id}), 201

# PUT /items/{item_id}
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in items:
        items[item_id] = request.get_json()
        return jsonify({'message': 'Item updated', 'item_id': item_id})
    else:
        return jsonify({'error': 'Item not found'}), 404

# DELETE /items/{item_id}
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({'message': 'Item deleted', 'item_id': item_id})
    else:
        return jsonify({'error': 'Item not found'}), 404

# Helper functions

def generate_cart_id():
    return str(uuid.uuid4())

def generate_order_id():
    return str(uuid.uuid4())

def generate_item_id():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run()

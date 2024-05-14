from flask import Flask, request, jsonify
from mobile_factory import MobileFactory

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    components = data.get('components', [])
    
    if not components:
        return jsonify({"error": "No components provided"}), 400

    order = MobileFactory.create_order(components)
    
    if order is None:
        return jsonify({"error": "Invalid order components"}), 400
    
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(debug=True)

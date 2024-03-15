# server.py

from flask import Flask, request, jsonify
from billing_logic import BillingSystem

app = Flask(__name__)
billing_system = BillingSystem()

@app.route('/calculate_total', methods=['POST'])
def calculate_total():
    data = request.get_json()
    total = billing_system.calculate_total(data['items'])
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(debug=True)

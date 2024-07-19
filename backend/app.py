from flask import Flask, request, jsonify
from model import generate_test_cases

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    code = data.get('code')
    test_cases = generate_test_cases(code)
    return jsonify({"test_cases": test_cases})

if __name__ == '__main__':
    app.run(debug=True)

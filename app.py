# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# This lets the frontend talk to this backend
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Takes a math expression from the frontend and returns the result.
    Expects JSON like: {"expression": "2+2"}
    """
    data = request.get_json()

    if not data or 'expression' not in data:
        return jsonify({'error': 'Invalid input format.'}), 400

    expression = data['expression']

    try:
        # eval() is used for simplicity here.
        # This is generally safe since our frontend buttons create the expression,
        # but for a public app, you'd want a more robust math parser.
        result = eval(expression)
        return jsonify({'result': result})
    except (SyntaxError, ZeroDivisionError):
        return jsonify({'error': 'Invalid calculation.'}), 400
    except Exception as e:
        # Catch any other unexpected issues
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An unknown error occurred.'}), 500

if __name__ == '__main__':
    # Start the development server
    app.run(host='0.0.0.0', port=5000, debug=True)

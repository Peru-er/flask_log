
from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/error', methods=['GET'])
def error():
    app.logger.error('An error occurred at /error route')
    return jsonify({"error": "Something went wrong"}), 500
  

if __name__ == '__main__':
    app.run(debug=True)


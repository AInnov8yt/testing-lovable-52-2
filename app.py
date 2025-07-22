from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from the Flask backend!"})

if __name__ == '__main__':
    app.run(debug=True)
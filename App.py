from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

data = []

@app.route('/')
def home():
    return "Server Running ✅"

@app.route('/save', methods=['POST'])
def save():
    entry = request.json
    data.append(entry)
    return jsonify({"message": "Saved successfully"})

@app.route('/download', methods=['GET'])
def download():
    df = pd.DataFrame(data)
    file_name = "coder_data.xlsx"
    df.to_excel(file_name, index=False)
    return send_file(file_name, as_attachment=True)

if __name__ == '__main__':
    app.run()

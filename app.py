from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

FILE_NAME = "data.xlsx"

@app.route('/')
def home():
    return "Server Running ✅"

@app.route('/save', methods=['POST'])
def save():
    new_data = request.json

    print("Received Data:", new_data)  # ✅ Debug log

    # ✅ Load existing file OR create new
    if os.path.exists(FILE_NAME):
        df = pd.read_excel(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["claimId","cpt","removed","added","A","B","C","D","E","F","G"])

    # ✅ Add new row
    df.loc[len(df)] = new_data

    # ✅ Save file
    df.to_excel(FILE_NAME, index=False)

    return jsonify({"message": "Saved successfully"})

@app.route('/download', methods=['GET'])
def download():
    if os.path.exists(FILE_NAME):
        return send_file(FILE_NAME, as_attachment=True)
    else:
        return "No data available"

if __name__ == '__main__':
    app.run()

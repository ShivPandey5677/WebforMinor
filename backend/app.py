from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/upload', methods=['POST'])
def upload():
    try:
        for series in ["series1", "series2", "series3"]:
            uploaded_files = request.files.getlist(f"{series}[]")
            print(f"Received {len(uploaded_files)} files for {series}")
            for file in uploaded_files:
                print(f"File: {file.filename}")
        return {"message": "Files uploaded successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(port=5000)

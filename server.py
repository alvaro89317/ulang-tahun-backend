from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server ulang tahun aktif 🎂"


@app.route("/jawaban", methods=["POST"])
def jawaban():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Data kosong"
        }), 400

    nama = data.get("jawaban", "")

    print("\n==============================")
    print("💌 JAWABAN BARU")
    print("==============================")
    print("Jawaban:", nama)
    print("==============================\n")

    return jsonify({
        "status": "success",
        "message": "Jawaban berhasil diterima 💕"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
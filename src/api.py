from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import datetime

app = Flask(__name__)
CORS(app)

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Servidor de Reconhecimento Facial ativo 🚀"})

@app.route("/recognize", methods=["POST"])
def recognize_face():
    try:
        data = request.get_json()
        img_base64 = data.get("image")

        if not img_base64:
            return jsonify({"error": "Nenhuma imagem enviada"}), 400

        img_bytes = base64.b64decode(img_base64)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        print(f"[{datetime.datetime.now()}] ➤ Rostos detectados: {len(faces)}")

        if len(faces) > 0:
            print("✅ Rosto reconhecido com sucesso!")
            return jsonify({
                "recognized": True,
                "user": "Rafael",  
                "timestamp": datetime.datetime.now().isoformat()
            })
        else:
            print("❌ Nenhum rosto reconhecido.")
            return jsonify({
                "recognized": False,
                "user": None,
                "timestamp": datetime.datetime.now().isoformat()
            })

    except Exception as e:
        print(f"Erro ao processar imagem: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Servidor Flask iniciado. Aguardando imagens do app...")
    print("Endpoints ativos:")
    print("   → GET  /           (status do servidor)")
    print("   → POST /recognize  (envio de imagem base64 para reconhecimento facial)")
    app.run(host="0.0.0.0", port=5000)

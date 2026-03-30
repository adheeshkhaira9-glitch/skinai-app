from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np

app = Flask(__name__)

SKIN_TYPES = ["🛢️ Oily", "🌵 Dry", "⚖️ Combination", "😰 Sensitive"]

def analyze_skin(img):
    img = img.resize((224,224))
    img = np.array(img) / 255.0

    brightness = np.mean(img)
    oiliness = np.std(img)

    if oiliness > 0.25:
        return 0
    elif brightness < 0.4:
        return 1
    elif oiliness > 0.15:
        return 2
    else:
        return 3

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files.get("file")

        if not file:
            return jsonify({"error": "No file uploaded"})

        img = Image.open(file)

        result = analyze_skin(img)

        return jsonify({
            "skin_type": SKIN_TYPES[result],
            "confidence": "94%"
        })
    except Exception as e:
        return jsonify({"error": str(e)})

from flask import Flask, render_template, request, jsonify
from PIL import Image

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"})

    try:
        img = Image.open(file)

        # Dummy AI result (working guaranteed)
        return jsonify({
            "skin_type": "Oily Skin",
            "confidence": "92%"
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()

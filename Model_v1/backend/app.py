from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import subprocess
import joblib
import os

app = Flask(__name__)
CORS(app)

# ── Base directory of this file (backend/) ─────────────────────────────────────
basedir = os.path.abspath(os.path.dirname(__file__))

# ── Load the trained SVM model and TF-IDF vectorizer from ../models-&-reports ──
model_path = os.path.join(basedir, "..", "models-&-reports", "spam_svm.pkl")
vectorizer_path = os.path.join(basedir, "..", "models-&-reports", "tfidf_vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# ── Ensure "db" directory exists under backend/ ────────────────────────────────
db_dir = os.path.join(basedir, "db")
os.makedirs(db_dir, exist_ok=True)

# ── Configure SQLite database ─────────────────────────────────────────────────
db_path = os.path.join(db_dir, "prompts.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ── Database model ─────────────────────────────────────────────────────────────
class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    classification = db.Column(db.String(10), nullable=False)

with app.app_context():
    db.create_all()

# ── Prediction endpoint ────────────────────────────────────────────────────────
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Text is required"}), 400

    transformed = vectorizer.transform([text])
    pred = model.predict(transformed)[0]
    return jsonify({"prediction": str(pred)})

# ── Save prompt endpoint ───────────────────────────────────────────────────────
@app.route("/api/savePrompt", methods=["POST"])
def save_prompt():
    data = request.get_json()
    text = data.get("text")
    classification = data.get("classification")
    if not text or not classification:
        return jsonify({"error": "Missing text or classification"}), 400

    new = Prompt(text=text, classification=classification)
    db.session.add(new)
    db.session.commit()
    return jsonify({"message": "Prompt saved successfully!"})

# ── Get all prompts ───────────────────────────────────────────────────────────
@app.route("/api/getPrompts", methods=["GET"])
def get_prompts():
    prompts = Prompt.query.all()
    return jsonify([
        {"id": p.id, "text": p.text, "classification": p.classification}
        for p in prompts
    ])

# ── Clear all prompts ─────────────────────────────────────────────────────────
@app.route("/api/clearPrompts", methods=["DELETE"])
def clear_prompts():
    Prompt.query.delete()
    db.session.commit()
    return jsonify({"message": "All prompts deleted"})

# ── Delete specific prompt by ID ──────────────────────────────────────────────
@app.route("/api/deletePrompt/<int:prompt_id>", methods=["DELETE"])
def delete_prompt(prompt_id):
    p = Prompt.query.get(prompt_id)
    if not p:
        return jsonify({"error": "Prompt not found"}), 404
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message": "Prompt deleted"})

# ── Function to start Next.js frontend automatically ──────────────────────────
def start_frontend():
    frontend_dir = os.path.join(basedir, "..", "frontend-Next.js")
    subprocess.Popen(["npm", "run", "dev"], cwd=frontend_dir)

if __name__ == "__main__":
    start_frontend()         # Launch your Next.js app
    app.run(debug=True, port=8000)

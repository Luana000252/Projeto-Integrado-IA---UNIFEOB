from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib, os
from utils.pii_detector import find_pii

app = Flask(__name__)
CORS(app)

MODEL_PATH = os.path.join('models','model.pkl')
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception:
        model = None

def risk_score(text):
    if model is not None:
        probs = model.predict_proba([text])[0]
        idx = probs.argmax()
        lab = model.classes_[idx]
        p = probs[idx]
        if lab == 'phishing' and p > 0.8:
            return 'Alto', float(p)
        if lab == 'phishing' and p > 0.5:
            return 'Médio', float(p)
        return 'Baixo', float(p)
    keywords = ['clique','link','confirm','pag','senha','cart','cartão','banco','atualize']
    s = text.lower()
    score = sum(1 for k in keywords if k in s)
    if score >= 3:
        return 'Alto', 0.9
    if score >= 1:
        return 'Médio', 0.6
    return 'Baixo', 0.2

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json() or {}
    text = data.get('text','')
    if not text:
        return jsonify({'error':'text vazio'}), 400
    pii = find_pii(text)
    risk, confidence = risk_score(text)
    return jsonify({'pii': pii, 'risk': risk, 'confidence': confidence})

@app.route('/')
def index():
    return 'API rodando. POST /analyze {"text":"..."}'

if __name__ == '__main__':
    app.run(debug=True)

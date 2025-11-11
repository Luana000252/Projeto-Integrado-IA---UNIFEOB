import sys, joblib, json

try:
    model = joblib.load('models/model.pkl')
except Exception:
    print('Modelo não encontrado. Rode python train.py primeiro.')
    raise SystemExit(1)

text = ' '.join(sys.argv[1:])
if not text:
    print('Passe o texto como argumento')
    raise SystemExit(1)

label = model.predict([text])[0]
prob = max(model.predict_proba([text])[0])
print(json.dumps({'label': label, 'confidence': float(prob)}))

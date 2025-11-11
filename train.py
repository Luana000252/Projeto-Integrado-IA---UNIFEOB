import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib, os

df = pd.read_csv('data/train.csv')

pipe = make_pipeline(TfidfVectorizer(), MultinomialNB())
pipe.fit(df['text'], df['label'])

os.makedirs('models', exist_ok=True)
joblib.dump(pipe, 'models/model.pkl')
print('Modelo treinado e salvo em models/model.pkl')

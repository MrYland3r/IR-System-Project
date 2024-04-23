from flask import Flask, request, jsonify
import pickle
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    top_k = request.json.get('top_k', 5)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('tfidf_matrix.pkl', 'rb') as f:
        tfidf_matrix = pickle.load(f)
    query_vec = vectorizer.transform([query])
    cos_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_k_indices = np.argsort(cos_sim)[-top_k:][::-1]
    results = {i: cos_sim[i] for i in top_k_indices}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
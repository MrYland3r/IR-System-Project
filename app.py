from flask import Flask, request, jsonify
import pickle
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get('query', '')
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('tfidf_matrix.pkl', 'rb') as f:
        tfidf_matrix = pickle.load(f)
    query_vec = vectorizer.transform([query])
    cos_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = np.argsort(cos_sim)[-5:][::-1]
    results = {index: cos_sim[index] for index in top_indices}
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
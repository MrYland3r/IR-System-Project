from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import json

def index_review():
    # Load reviews from file
    with open('reviews.json', 'r') as file:
        reviews = json.load(file)
    documents = [review['review'] for review in reviews]

    # Create TF-IDF index
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

if __name__ == '__main__':
    index_reviews()

from sklearn.feature_extraction.text import TfidVectorizer
import pickle

class Indexer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    
    def create_index(self, documents):
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        # Save the vectorizer and matrix for querying
        pickle.dump(self.vectorizer, open('vectorizer.pkl', 'wb'))
        pickle.dump(tfidf_matrix, open('tfidf_matrix.pkl', 'wb'))
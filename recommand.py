import json
import numpy as np
from sklearn.neighbors import NearestNeighbors
import scipy.sparse as sp
import spacy

nlp = spacy.load('en_core_web_sm')

# Pre-process text
def preprocessText(text):
    doc = nlp(text.lower())
    cleanedTokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(cleanedTokens)

# Loading precomputed TF-IDF data 
def loadTfidfData(tfidfFile='tfidfData.npz', metadataFile='tfidfData.json'):
    tfidfMatrix = sp.load_npz(tfidfFile)
    with open(metadataFile, 'r') as f:
        tfidfData = json.load(f)
    
    return tfidfMatrix, tfidfData['featureNames'], tfidfData['books']

# Vectorize input text using precomputed vocabulary
def vectorizeInputText(inputTitle, featureNames):
    processedTitle = preprocessText(inputTitle)
    inputVector = np.zeros(len(featureNames))  # Creating zero-vector for input
    
    # Tokenize text and checking for matching terms in the vocabulary
    for word in processedTitle.split():
        if word in featureNames:
            idx = featureNames.index(word)
            inputVector[idx] += 1  # Count word
    
    return inputVector.reshape(1, -1)  # Return 2D Array

# Content-based Recommendation Function using k-NN 
def contentBasedRecommendations(title, nNeighbors=5): # Limmiting the number of returned recommendations to 20
    tfidfData = loadTfidfData()
    tfidfMatrix, featureNames, books = tfidfData
    inputVector = vectorizeInputText(title, featureNames)

    # k-NN model
    knn = NearestNeighbors(n_neighbors=nNeighbors, metric='cosine')  # Using cosine similarity
    knn.fit(tfidfMatrix)
    
    # Finding the k nearest neighbors 
    distances, indices = knn.kneighbors(inputVector)
    
    # Getting recommended books based on the indices
    recommendedEntries = [books[i] for i in indices.flatten()]
    
    # Sorting recommendations by distance where smaller distance is higher simmiarity
    sortedRecommendations = [recommendedEntries[i] for i in np.argsort(distances.flatten())]
    
    return sortedRecommendations # Return sorted recommendations 

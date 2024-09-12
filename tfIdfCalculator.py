import pandas as pd
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
import scipy.sparse as sp

nlp = spacy.load('en_core_web_sm')

# Pre-processing text
def preprocessText(text):
    doc = nlp(text.lower())
    cleanedTokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(cleanedTokens)

# Combining columns 
def combineColumns(row):
    combinedText = ' '.join([
        str(row['Title']), 
        str(row['Authors']), 
        str(row['Category']), 
        str(row['Description'])
    ])
    return combinedText

def CalcTfidfData(filePath='tfidfData.npz'):
    # Check if the files exist
    if os.path.exists(filePath) and os.path.exists(filePath.replace('.npz', '.json')):
        print(f"TF-IDF data already saved to {filePath} and {filePath.replace('.npz', '.json')}. Skipping processing.")
        return
    # Loading data
    bookList = pd.read_csv('BooksDataset.csv') 
    # Preprocessing combined text 
    bookList['combinedText'] = bookList.apply(combineColumns, axis=1).fillna('').apply(preprocessText)   
    # Creating TF-IDF vectorizer
    tfidf = TfidfVectorizer()   
    # Fitting the TF-IDF model and transformming data
    tfidfMatrix = tfidf.fit_transform(bookList['combinedText'])
    # Extracting feature names
    tfidfFeatures = tfidf.get_feature_names_out().tolist()    
    # SaveTF-IDF matrix using sparse matrix format
    sp.save_npz(filePath.replace('.json', '.npz'), tfidfMatrix)   
    # Separately save the feature names and book metadata 
    tfidfData = {
        'featureNames': tfidfFeatures,
        'books': bookList[['Title', 'Authors', 'Category', 'Publish Date', 'Price']].to_dict(orient='records')
    }
    
    with open(filePath.replace('.npz', '.json'), 'w') as f:
        json.dump(tfidfData, f)

    # Calling Function once to create and save TfIdf data 
    CalcTfidfData()
    print("TF-IDF data saved to tfidfData.npz and tfidfData.json")
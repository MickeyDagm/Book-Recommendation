
Book Recommendation System
The system is an AI-driven Book Suggestion System that employs the K-Nearest Neighbors (KNN) algorithm to suggest similar books based on various features such as the title, author, category, and description. By pre-processing and converting book data into numerical form such as TF-IDF vector, the system identifies books that are closely related to the user's input. This method allows the system to recommend titles that share similar characteristics, including those with similar names, providing users with relevant and precise suggestions.

Features
Content-based recommendations: analyze the features of books such as the title, author, category, and description, and uses the  K-Nearest Neighbors (KNN) algorithm to suggest similar books.
User Interface: This simple standalone desktop application is developed using `Tkinter` where users can input a book title and receive recommendations.

Files and Directories
-`app.py`: The main file holding the desktop application where users input the book title and get recommendations.
-`recommand.py`: This file containing the main logic for computing the Content-based recommendations and return the recommondations.
-`vectorizer.py`: This file preprocesses the book data and computes the TF-IDF vector and saves them into `.npz` and `.json` files.
-`BooksDataset.csv`: The dataset containing book list.
-`README.md`: The file containg the explation, feature and usage of the proram.
The precomputed TF-IDF matrix and feature names are stored in two files:
    -`tfidfData.npz`: The TF-IDF sparse matrix of the book metadata.
    -`tfidfData.json`: The metadata of books including the feature names and information about each book.
These files are generated using `vectorizer.py`.

Installation and Setup
1. Create a virtual environment and activate it:
    `python -m venv .venv`
    On Unix or MacOS  `source .venv/bin/activate` 
    On Windows `.venv\Scripts\activate`
2. Install all the required dependencies:
    `pip install -r requirements.txt`
3. Download the necessary language model for `spacy`:
    `python -m spacy download en_core_web_sm`
4. Run the application:
    `python app.py`





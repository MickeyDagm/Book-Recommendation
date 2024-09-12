import tkinter as tk
from tkinter import messagebox, ttk
from recommand import  contentBasedRecommendations

class BookRecommendationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Recommendation System")
        self.geometry("1000x400")

        # Setup the main frame
        self.mainFrame = tk.Frame(self)
        self.mainFrame.pack(expand=True, fill="both")

        # Create UI elements
        self.createWidgets()
        
    def createWidgets(self):
        # Book title entry 
        tk.Label(self.mainFrame, text="Enter the book title:", font=("Helvetica", 12)).pack(pady=10)
        self.titleEntry = tk.Entry(self.mainFrame, width=50)
        self.titleEntry.pack(pady=10)

        # Submit button
        tk.Button(self.mainFrame, text="Get Recommendations", command=self.getRecommendations).pack(pady=10)

        # Results Table
        self.resultTree = ttk.Treeview(self.mainFrame, columns=("Title", "Authors", "Category", "Publish Date", "Price"), show='headings')
        self.resultTree.heading("Title", text="Title")
        self.resultTree.heading("Authors", text="Authors")
        self.resultTree.heading("Category", text="Category")
        self.resultTree.heading("Publish Date", text="Publish Date")
        self.resultTree.heading("Price", text="Price")
        self.resultTree.pack(pady=20, fill=tk.BOTH, expand=True)
    
    def getRecommendations(self):
        title = self.titleEntry.get().strip()
        # Check if title is entered
        if not title:
            messagebox.showwarning("Input Error", "Please enter a book title.")
            return
        
        # Generating recommendations 
        recommendations = contentBasedRecommendations(title)

        # Updating Results Table by recommendations
        self.updateResults(recommendations)
    
    def updateResults(self, recommendations):
        # Clearing current results
        for row in self.resultTree.get_children():
            self.resultTree.delete(row)
        
        # Inserting new results
        for rec in recommendations:
            self.resultTree.insert("", tk.END, values=(rec['Title'], rec['Authors'], rec['Category'], rec['Publish Date'], rec['Price']))
    
if __name__ == "__main__":
    app = BookRecommendationApp()
    app.mainloop()

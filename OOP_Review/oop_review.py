
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    
    def display_details(self):
        print(f"Title:{self.title}, Author: {self.author}, Pages: {self.pages} \nIs a long book: {self.is_long_book()}")
        
    def is_long_book(self):
        return self.pages > 100
    
    
Book1 = Book("Python Programming", "John Doe", 80)
Book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
Book3 = Book("Short Stories", "Jane Smith", 95)
    
Book1.display_details()
print()

Book2.display_details()
print()

Book3.display_details()
print()

    
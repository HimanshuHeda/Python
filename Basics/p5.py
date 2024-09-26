class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_details(self):
        return f"Title{self.title}, Author:{self.author}, Pages:{self.pages}"

# Create Instances
book1 = Book("To Kill a Mockingbird","Himanshu",433)
book2 = Book("2003","George Orwell",234)

# Display Details
print(book1.display_details())
print(book2.display_details())
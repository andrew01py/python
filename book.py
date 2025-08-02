# Base class
class Book:
    def _init_(self, title, author, pages):
        self.title =("Alchemist")
        self.author =("andrew01py")
        self._pages = 50

    def get_summary(self):
        return f"'{self.title}' by {self.author}, {self._pages} pages."

    def read(self):
        return f"You start reading '{self.title}'..."

# Subclass (inherits from Book)
class EBook(Book):
    def _init_(self, title, author, pages, file_size):
        super()._init_(title, author, pages)
        self.file_size = file_size  # in MB

    def get_summary(self):
        # Polymorphism: overrides method from base class
        return f"E-Book: '{self.title}' by {self.author}, {self._pages} pages, {self.file_size}MB."

    def download(self):
        return f"Downloading '{self.title}'... ({self.file_size}MB)"

# Test the classes
book1 = Book
ebook1 = EBook

print(book1.get_summary("book"))
print(book1.read())

print(ebook1.get_summary())
print(ebook1.download())
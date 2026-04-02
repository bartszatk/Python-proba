class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available


class Library:
    def __init__(self, filename):
        self.filename = filename

    def add_book(self, title, author, year):
        with open(self.filename, "a") as f:
            f.write(f"{title};{author};{year};1\n")

    def show_books(self):
        with open(self.filename, "r") as f:
            for line in f:
                title, author, year, available = line.strip().split(";")
                print(title, author, year, "Available" if available == "1" else "Taken")

    def borrow_book(self, title):
        lines = []
        with open(self.filename, "r") as f:
            for line in f:
                t, a, y, av = line.strip().split(";")
                if t == title and av == "1":
                    av = "0"
                lines.append(f"{t};{a};{y};{av}\n")

        with open(self.filename, "w") as f:
            f.writelines(lines)

    def return_book(self, title):
        lines = []
        with open(self.filename, "r") as f:
            for line in f:
                t, a, y, av = line.strip().split(";")
                if t == title:
                    av = "1"
                lines.append(f"{t};{a};{y};{av}\n")

        with open(self.filename, "w") as f:
            f.writelines(lines)


lib = Library("books.txt")

lib.add_book("Python", "Guido", 1991)
lib.add_book("C++", "Bjarne", 1985)

lib.borrow_book("Python")
lib.return_book("Python")

lib.show_books()

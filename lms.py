class library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def listBooks(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        if not lines:
            print("» No books available.\n")
            return
        for line in lines:
            info = line.split(',')
            print(f"» Book Name: {info[0]}, Author: {info[1]}, Release Date: {info[2]}, Number of Pages: {info[3]}")
        
    def addBook(self):
        name = input("\n» Enter book title: ")
        author = input("» Enter book author: ")
        date = input("» Enter release year: ")
        pages = input("» Enter number of pages: ")
        info = f"{name},{author},{date},{pages}\n"
        self.file.write(info)
        print("\n» Book added successfully.\n")
    
    def removeBook(self):
        title = input("\n» Enter the title of the book to remove: ")
        self.file.seek(0)
        lines = self.file.readlines()
        updatedLines = [line for line in lines if title not in line]
        if len(updatedLines) == len(lines):
            print(f"\n» Book '{title}' not found.")
            return
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updatedLines)
        print(f"\n» Book '{title}' removed successfully.")

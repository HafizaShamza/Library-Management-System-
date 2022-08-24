class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
        listOfBooks.sort()

    def book_List(self):
        print("-----List of Books----- ")
        for book in self.books:
            # print("The List of Books is")
            print("  =>", book)

    def borrow_Book(self,BookName):
        if BookName in self.books:
            print(f"Congratualtions {BookName} Book is issued you. Please stay safe it and returned it, under 30 days. ")    
            self.books.remove(BookName)
            return BookName.sort()
            return True
        else:
            print("Sorry, This book is issued some one or some chances that this book is not available so wait until they available.")
            return False

    def returned_Book(self,BookName):
        print("Thanks for returning the book, Hope so you enjoy this book. Have a Good Day")
        self.books.append(BookName)

    def add_Book(self,BookName):
        print("Thanks for donating the interesting book.")
        self.books.append(BookName)

class Student:
    def Take_Book(self):
        self.book=input("Enter the book name which you want to borrow: ")
        return self.book
    def return_Book(self):
        self.book=input("Enter the book name which you returned: ")
        
        return self.book
    def donate_Book(self):
        self.book=input("Enter the book name which you want to donate: ")
        return self.book


if __name__ == "__main__":
    student=Student()
    centralLibrary=Library(["DSA" , "CA" , "LA" , "BBA" , "Mr.Chips"])
    # centralLibrary.book_List()


    # Now we preparing Menu card

    while(True):
        menuCard='''\n ======Welcome to My_Baaba Library======
        1-List of Book
        2-Request for Book
        3-Returned a Book
        4-Donate some Book
        5-Exit the System
        '''
        print(menuCard)
        a= int(input("Enter your choice: "))
        if a == 1:
            centralLibrary.book_List()
        elif a == 2:
            centralLibrary.borrow_Book(student.Take_Book())
        elif a == 3:
            centralLibrary.returned_Book(student.return_Book())
        elif a == 4:
            centralLibrary.add_Book(student.donate_Book())
        elif a == 5:
            print("**Thanks for choosing the My_Baaba Library!**")
            exit()
        else:
            print("Invalide Choice")

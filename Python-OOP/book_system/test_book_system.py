import unittest
from os import name

from book_system.book import Book
from book_system.member import Member
from book_system.librarian import Librarian
from book_system.loan import Loan


class TestBook(unittest.TestCase):
    def test_book_is_created_with_correct_details(self):
        book_one = Book(1, "The wise man", "Kenny", 100)
        self.assertEqual(1, book_one.book_id)
        self.assertEqual("The wise man", book_one.title)
        self.assertEqual("Kenny", book_one.author)
        self.assertEqual(100, book_one.isbn)

    def test_book_can_be_borrowed(self):
        book_one = Book(1, "The wise man", "Kenny", 100)
        book_one.borrow_book()
        self.assertFalse(book_one.borrow_book())


    def test_book_availability_changes_after_borrowing(self):
       book_one = Book(1, "The wise man", "Kenny", 100)

       book_one.borrow_book()
       self.assertFalse(book_one.isAvailable)
       book_one.return_book()
       self.assertTrue(book_one.isAvailable)


    def test_that_book_is_available(self):
        book_one = Book(1, "The wise man", "Kenny", 100)
        self.assertTrue(book_one.is_available())


    def test_that_one_book_created_and_test_to_get_the_book_details(self):
        book_one = Book(1, "The wise man", "Kenny", 100)
        details = book_one.get_book_details()

        self.assertEqual(1, details["book_id"])
        self.assertEqual("The wise man", details["title"])
        self.assertEqual("Kenny", details["author"])
        self.assertEqual(100, details["isbn"])


    def test_that_two_books_created_test_to_get_the_two_books_details(self):
        book_one = Book(1, "The wise man", "Kenny", 100)
        book_two = Book(2, "The young shall grow", "Smart", 101)

        book_one_details = book_one.get_book_details()
        self.assertEqual(1, book_one_details["book_id"])
        self.assertEqual("The wise man", book_one_details["title"])
        self.assertEqual("Kenny", book_one_details["author"])
        self.assertEqual(100, book_one_details["isbn"])


        book_two_details = book_two.get_book_details()
        self.assertEqual(2, book_two_details["book_id"])
        self.assertEqual("The young shall grow", book_two_details["title"])
        self.assertEqual("Smart", book_two_details["author"])
        self.assertEqual(101, book_two_details["isbn"])


    def test_that_three_books_created_and_test_to_update_one_book(self):
        book_one = Book(1, "The wise man", "Kenny", 100)
        book_two = Book(2, "The young shall grow", "Smart", 101)
        book_three = Book(3, "Winners never quit", "Kehinde", 102)


        book_two.update_book("Life is a lesson", "Olatunji Smart", 113)
        self.assertEqual("Life is a lesson", book_two.title)
        self.assertEqual("Olatunji Smart", book_two.author)
        self.assertEqual(113, book_two.isbn)








class TestLibrarian(unittest.TestCase):
    def test_to_create_librarian_details(self):
        librarian_one = Librarian("001", "Ojo Ade", "adeojo@gmail.com", "OJO/001", "Semicolon" )

        self.assertEqual("001", librarian_one.librarian_id)
        self.assertEqual("Ojo Ade", librarian_one.librarian_name)
        self.assertEqual("adeojo@gmail.com", librarian_one.librarian_email)
        self.assertEqual("Semicolon", librarian_one.library_name)

    def test_librarian_can_add_book_to_the_library(self):
        librarian_one = Librarian("001", "Ojo Ade", "adeojo@gmail.com", "OJO/001", "Semicolon" )

        


class TestMember(unittest.TestCase):

    ...

class TestLoan(unittest.TestCase):
    ...


if __name__ == '__main__':
    unittest.main()

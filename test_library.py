import pytest
from library import Library  # Stellen Sie sicher, dass Sie die richtigen Modulnamen verwenden
from book import Book
from customer import Customer
import random

class TestLibrary:

    @pytest.fixture
    def sample_library(self):
        return Library()

    @pytest.fixture
    def customer_max(self, sample_library):
        return Customer('Max', None, sample_library)

    @pytest.fixture
    def customer_moritz(self, sample_library):
        return Customer('Moritz', None, sample_library)

    @pytest.fixture
    def book_1(selfself):
        book = Book('Adam', 123)
        book.location = 'AB1'
        return book

    @pytest.fixture
    def book_2(selfself):
        book = Book('Eva', 987)
        book.location = 'XY9'
        return book


    def test_add_and_print_customers(self, sample_library, customer_max, customer_moritz, capsys):

        sample_library.print_customer()
        captured = capsys.readouterr()
        assert 'Kunden:\nKunde: Max\nKunde: Moritz\n---\n' in captured.out

    def test_search_customer(self, sample_library, customer_max, customer_moritz):
        sample_library.add_customer(customer_max)
        sample_library.add_customer(customer_moritz)
        customer = sample_library.search_customer('Moritz')
        assert customer is customer_moritz

    def test_search_customer_failed(self, sample_library, customer_max, customer_moritz):
        sample_library.add_customer(customer_max)
        sample_library.add_customer(customer_moritz)
        customer = sample_library.search_customer('Julian')
        assert customer is None


    def test_add_book_and_print_invetory(self, sample_library, book_1, book_2, capsys):
        sample_library.add_book(book_1)
        sample_library.add_book(book_2)
        sample_library.print_inventory()
        captured = capsys.readouterr()
        assert 'Inventar:\nISBN : 123 / Titel: Adam  / Ablage : AB1\nISBN : 987 / Titel: Eva  / Ablage : XY9\n' in captured.out

    def test_search_book(self, sample_library, book_1, book_2):
        sample_library.add_book(book_1)
        sample_library.add_book(book_2)
        book = sample_library.search_book_by_title('Adam')
        assert book.title == 'Adam'
        assert book.isbn == 123
        assert book.location == 'AB1'

    def test_search_book_failed(self, sample_library, book_1, book_2):
        sample_library.add_book(book_1)
        sample_library.add_book(book_2)
        book = sample_library.search_book_by_title('Tuti')
        assert book is None

    def test_remove_book(self, sample_library, book_1, book_2):
        sample_library.add_book(book_1)
        sample_library.add_book(book_2)
        sample_library.remove_book(book_2)
        book = sample_library.search_book_by_title('Eva')
        assert book is None
        book = sample_library.search_book_by_title('Adam')
        assert book is book_1

    def test_borrow_book(self, sample_library, book_1, book_2):
        sample_library.add_book(book_1)
        sample_library.add_book(book_2)
        borrowed_book = sample_library.borrow_book('AB1')
        assert borrowed_book is book_1
        book = sample_library.search_book_by_title('Adam')
        assert book is None

    def test_put_back_book(self, sample_library, book_1, book_2):
        sample_library.add_book(book_1)
        sample_library.put_back_book(book_2)
        book = sample_library.search_book_by_title('Eva')
        assert book is book_2
        book = sample_library.search_book_by_title('Adam')
        assert book is book_1

if __name__ == '__main__':
    pytest.main()
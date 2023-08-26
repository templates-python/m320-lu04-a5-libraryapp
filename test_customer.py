import pytest
from library import Library  # Stellen Sie sicher, dass Sie die richtigen Modulnamen verwenden
from book import Book
from customer import Customer
from librarian import Librarian


class TestCustomer:

    @pytest.fixture
    def sample_library(self):
        return Library()

    @pytest.fixture
    def pit(self, sample_library):
        return Librarian('Pit', sample_library)


    @pytest.fixture
    def customer_max(self, sample_library, pit):
        return Customer('Max', pit, sample_library)


    def test_print_customer(self, customer_max, capsys):
        customer_max.print()
        captured = capsys.readouterr()
        assert captured.out == 'Kunde: Max\n'

    def test_borrow_a_book_by_title(self, customer_max, pit):
        pit.buy_new_book('Test Titel', 'ABC-123')
        customer_max.borrow_a_book_by_title('Test Titel')
        book = customer_max.get_borrowed_book()
        assert book.title == 'Test Titel'

    def test_bring_back_a_book(self, customer_max, sample_library, pit):
        pit.buy_new_book('Test', 'ABC-123')
        customer_max.borrow_a_book_by_title('Test')
        customer_max.bring_back_a_book()
        book = sample_library.search_book_by_title('Test')
        assert book.title == 'Test'
        assert customer_max.get_borrowed_book() == None
import pytest
from library import Library  # Stellen Sie sicher, dass Sie die richtigen Modulnamen verwenden
from book import Book
from customer import Customer
from librarian import Librarian


class TestLibrarian:

    @pytest.fixture
    def sample_library(self):
        return Library()

    @pytest.fixture
    def pit(self, sample_library):
        return Librarian('Pit', sample_library)

    @pytest.fixture
    def customer_max(self, pit,sample_library):
        return Customer('Max', pit, sample_library)

    def test_buy_new_book(self, sample_library, pit):
        pit.buy_new_book('Test Titel', 'ABC-123')
        book = sample_library.search_book_by_title('Test Titel')
        assert book.title == 'Test Titel'
        assert book.isbn == 'ABC-123'
        assert book.location is not None  #es muss ein String mit einem Ablageort hinterlegt sein.


    def test_borrow_a_book_by_title(self, sample_library, pit):
        pit.buy_new_book('Test Titel', 'ABC-123')
        book = pit.borrow_a_book_by_title('Test Titel')
        assert book.title == 'Test Titel'
        assert book.isbn == 'ABC-123'
        assert book.location is not None  # es muss ein String mit einem Ablageort hinterlegt sein.

    def test_get_a_book_from_customer(self, sample_library, pit):
        book = Book(title='Test', isbn='ABC-789')
        pit.get_a_book_from_customer(book)
        book = sample_library.search_book_by_title('Test')
        assert book.title == 'Test'

    def test_remind_customer(self, pit, customer_max):
        pit.buy_new_book('Test Titel', 'ABC-123')
        book = customer_max.borrow_a_book_by_title('Test Titel')
        customer_max.remind()
        assert customer_max.is_reminded() == True

    def test_remove_book(self, sample_library, pit):
        pit.buy_new_book('Test Titel', 'ABC-123')
        book = sample_library.search_book_by_title('Test Titel')
        assert book.title == 'Test Titel'
        pit.remove_book('Test Titel')
        book = sample_library.search_book_by_title('Test Titel')
        assert book == None






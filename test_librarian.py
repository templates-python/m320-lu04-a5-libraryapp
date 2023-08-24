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





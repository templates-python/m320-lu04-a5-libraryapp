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



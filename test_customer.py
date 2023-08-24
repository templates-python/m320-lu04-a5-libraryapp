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





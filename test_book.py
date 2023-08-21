import pytest
import pytest
from book import Book  # Stellen Sie sicher, dass Sie den richtigen Modulnamen verwenden

class TestBook:

    @pytest.fixture
    def sample_book(self):
        return Book('Sample Book', '1234567890')

    def test_initialization(self, sample_book):
        assert sample_book.title == 'Sample Book'
        assert sample_book.isbn == '1234567890'
        assert sample_book.location is None

    def test_location(self, sample_book):
        sample_book.location = 'Shelf 1'
        assert sample_book.location == 'Shelf 1'

    def test_print(self, sample_book, capsys):
        sample_book.location = 'Shelf 2'
        sample_book.print()
        captured = capsys.readouterr()
        assert captured.out == 'ISBN : 1234567890 / Titel: Sample Book  / Ablage : Shelf 2\n'

if __name__ == '__main__':
    pytest.main()
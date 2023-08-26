from library import Library
from book import Book
from library import Library


class Librarian:
    """
    Die Klasse repräsentiert den Bibliothekar.
    Der Bibliothekar;

    * kauft neue Bücher ein, buy_new_book(...)
    * leiht Bücher dem Kunden aus, borrow_a_book_by_title(...)
    * nimmt Bücher zurück, get_a_book_from_customer(...)
    * mahnt den Kunden, remind_customer(...)
    * entfernt Bücher aus der Bibliothek, remove_book(...)

    """

    def __init__(self, name, library):
        """
        Erzeugt das Bibliothekar-Objekt und initialisiert es mit dem Namen des Bibliothekars.
        Es wird die Referenz zur Bibliothek im entsprechenden Attribut festgehalten.
        :param name: Name der Person (des Bibliothekars)
        :param library: Referenz zu Bibliothek-Objekt
        """
        # Initialisieren Sie hier die Attribute für name und library.
        # TODO

    def buy_new_book(self, title, isbn):
        """
        Ein neues Buch mit Titel und ISBN-Nummer wird der Bibliothek beigefügt.
        Die Methode erstellt ein neues Buch und fügt es der Bibliothek zu.
        Von der Bibliothek wird der Ablageort mitgeteilt, der dann dem Buch übergeben wird.
        :param title: Titel des Buchs
        :param isbn:  ISBN-Nummer des Buchs
        """
        # hier ein Buch-Objekt erzeugen, der Bibliothek zufügen und dann noch
        # den Ablageort (location) eintragen.
        # Beachten Sie das Book eine @dataclass repräsentiert und daher die
        # Parameter namentlich angegeben werden. Vergleichen Sie dazu die Theorie
        # in Kapitel 1 zu Dataclass
        # TODO

    def borrow_a_book_by_title(self, title):
        """
        Das angefragte Buch wird dem Kunden ausgeliehen.
        Ist das Buch nicht vorhanden, wird der Wert None geliefert.
        In diesem Fall gibt der Bibliothekar einen Hinweis aus.
        :param title: Titel des zur Ausleihe angefragten Buchs
        :return: eine Referenz auf ein Book-Objekt oder None, wenn der Titel nicht in der Bibliothek steht
        """
        # Pit sucht in der Bibliothek nach dem Buch (anhand des Titels). Danach holt er
        # sich beim Buch dessen Ablageort und leiht das Buch in der Bibliothek aus.
        # Sollte das Buch nicht existieren, gibt Pit eine Meldung aus, z.B. "Das angefragte Buch ist nicht vorhanden."
        # TODO

    def get_a_book_from_customer(self, borrowed_book):
        """
        Das gelieferte Buch wird in die Bibliothek zurückgestellt.
        :param borrowed_book: Buch das in die Bibliothek zurückgestellt wird
        """
        # Der Bibliothekar stellt das Buch zurück in die Bibliothek.
        # TODO

    def remind_customer(self, name):
        """
        Erinnert den Kunden, dass eine Ausleihe noch offen ist.
        :param name: Name des Kunden, der erinnert wird.
        """
        # Der Bibliothekar erinnert den Kunden an eine offene Ausleihe.
        # Er mittels Name des Kunden nach seiner Referenz in der Bibliothek,
        # damit er die Erinnerung durchführen kann.
        print(f'Erinnerung für {name}')
        # TODO

    def remove_book(self, title):
        """
        Entfernt ein Buch aus der Bibliothek. Das Buch wird anhand seines Titels identifiziert.
        :param title: Titel des gesuchten Buchs
        """
        print(f'\n---\nentferne Buch "{title}"')
        # TODO
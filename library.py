import random


class Library:
    """
    Ein Bibliothek-Objekt, das Informationen zu Büchern verfügbar macht.
    Die Bibliothek bietet Services für
    - zufügen von Büchern
    - löschen von Büchern
    - ausleihen von Büchern (Ausgabe und Rücknahme)
    - registrieren von Kunden
    an.
    Über die Ausgabe des Inventars ist jederzeit eine Übersicht der Bücher verfügbar.
    """

    def __init__(self):
        """
        Initialisiert
        * eine Liste für die verschiedenen Buch-Objekte
        * eine Liste für die Kunden-Objekte
        """
        self._booklist  = []
        self._customers = []

    def print_inventory(self):
        """
        Gibt den aktuellen Stand der Bücher in der Bibliothek auf dem Stdout aus.
        """
        print('Inventar:')
        for book in self._booklist:
            book.print()
        print('---')

    def add_customer(self, customer):
        """
        Fügt einen Kunden der Kundenliste zu.
        :param customer: ein Kunde
        """
        self._customers.append(customer)

    def search_customer(self, name):
        """
        Liefert das Kundenobjekt zum angegebenen Namen.
        :param name: Name des gesuchten Kundenobjekts
        :return: Kundenobjekt oder None, wenn der Name nicht gefunden wird
        """
        for customer in self._customers:
            if customer.name == name:
                return customer
        return None

    def print_customer(self):
        """
        Gibt eine Liste der Kunden auf dem Stdout aus.
        """
        print('Kunden:')
        for customer in self._customers:
            customer.print()
        print('---')

    def add_book(self, a_book):
        """
        Fügt ein Buch der Bibliothek zu und liefert die Position innerhalb der Bibliothek zurück.
        :param a_book: ein Buch
        :return: Position des Buchs
        """
        self._booklist.append(a_book)
        return chr(random.randint(65,68)) + str(random.randint(1,10))

    def remove_book(self, book):
        """
        Entfernt ein Buch aus der Bibliothek. Das Buch wird anhand seiner Referenz identifiziert.
        :param book: Das Buch das entfernt wird
        """
        self._booklist.remove(book)

    def search_book_by_title(self, title):
        """
        Sucht nach einem Buch in der Bibliothek.
        Die Suche erfolgt anhand des Buchtitels.
        :param title: Titel des Buchs
        :return: Referenz auf das Buch oder None, wenn es nicht gefunden wurde
        """
        for book in self._booklist:
            if book.title == title:
                return book
        return None

    def borrow_book(self, location):
        """
        Leiht ein Buch aus der Bibliothek aus.
        Das Buch wird anhand des Ablageortes aus der Bibliothek ausgetragen.
        :param location: Ablageort des Buchs
        :return: Referenz auf das Buch
        """
        for book in self._booklist:
            if book.location == location:
                # Buch aus der Liste entfernen und dem Aufrufer liefern
                self._booklist.remove(book)
                return book

    def put_back_book(self, borrowed_book):
        """
        Legt ein Buch zurück in die Bibliothek. Das Buch wird über seine Referenz identifiziert.
        Der Ablageort ist im Buch vermerkt und dient dazu. das Buch am richtigen Ort einzufügen.
        :param borrowed_book: Buch das in die Bibliothek zurückgestellt wird
        """
        self._booklist.append(borrowed_book)

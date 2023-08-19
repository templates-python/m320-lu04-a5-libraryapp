class Customer:
    '''
    Die Klasse beschreibt einen Kunden mit Namen, der in der Bibliothek ein Buch
    * ausleihen [ borrow_a_book_by_title() ] oder
    * zurückgeben [ bring_back_a_book() ]
    will.
    Die Ausleihe begrenzt sich pro Kunde auf ein Buch.
    Der Kunde kann gemahnt werden.

    Der Kunde kennt den Bibliothekar --> es gibt eine Referenz auf ein Librarian-Objekt

    Author  : René Probst
    Date    : 31.08.2022
    Version : 1.0
    Changed : ...
    '''

    def __init__(self, name, librarian, library):
        '''
        Initialisiert ein Objekt vom Typ Kunden mit dem Namen des Kunden und legt die Referenz
        zu einem Librarian-Objekt fest.
        :param name: Name des Kunden
        :param librarian: Referenz zum Bibliothekar
        '''
        #
        # Initialisieren Sie hier die Attribute für name, librarian und library.
        # Erstellen Sie die Referenz zum Library-Objekt, in dem sie die eigene
        # Referenz (self) mit der Methode add_customer() zuweisen.
        #
        # TODO
        self.name = name


    def print(self):
        '''
        Gibt den Namen des Kunden aus
        '''
        print("Kunde: " + self.name)

    @property
    def name(self):
        '''
        Liefert den Namen des Kunden.
        :return: Name des Kunden
        '''
        return self._name

    def borrow_a_book_by_title(self, title):
        '''
        Bezieht beim Bibliothekar das Buch, dessen Titel mitgegeben wird.
        Ist das Buch verfügbar, wird die Referenz abgespeichert.
        Andernfalls (Referenz ist null) wird eine entsprechende Meldung ausgegeben.

        Der Titel des gewünschten Buches wird dem Bibliothekar mitgeteilt.
        :param title: Titel des Buchs
        '''
        # Die Kundin fordert beim Bibliothekar ein Buch an und sagt, welchen Titel sie will.
        # Sie hat dann die Referenz auf das Buch.
        # TODO
        print(self._name + " hat das Buch '" + self._book.title + "' erhalten.")

    def bring_back_a_book(self):
        '''
        Bringt dem Bibliothekar das ausgeliehene Buch zurück.
        Nach der Rückgabe des Buchs wird die Referenz auf None gesetzt.
        '''
        # Die Kundin gibt das Buch dem Bibliothekar zurück.
        # Sie hat die Referenz auf das Buch, das sie ausgeliehen hat.
        # TODO
        print(self._name + " hat das Buch '" + self._book.title + "' zurückgebracht")

    def get_borrowed_book(self):
        '''
        Liefert das Buch, das durch den Kunden ausgeliehen wurde.
        :return: Referenz zum Buch
        '''
        return self._book

    def remind(self):
        '''
        Erinnerung, dass ein Buch noch ausstehend ist
        '''
        print("Das Buch '" + self._book.title + "' ist noch ausstehend")

from library import Library
from customer import Customer
from librarian import Librarian
from book import Book

'''
Bibliothek-Applikation ...
Author  : René Probst
Date    : 31.8.2022
Version : 1.0
Changed :
'''
def main():
    print("Bibliotheks-Anwendung\n=====================\n")
    # Objekte erzeugen und die Kundenliste ausgeben.
    # Teil 1
    # TODO
    library = Library()
    pit = Librarian('Pit', library)
    moritz = Customer('Moritz', pit, library)
    ursula = Customer('Ursula', pit, library)
    library.print_customer()

    # pit kauft 5 neue Bücher, die er der Bibliothek beifügt.
    # Danach wird das Inventar der Bibliothek ausgegeben.
    # Achtung: Die Klasse Book ist als @dataclass definiert. D.h. dass
    # im Konstruktor jeweils der Name des Attributs angegeben werden uss.
    # z.B. b = Book(title='Ein Titel', isbn='ABC-123')
    # Teil 2
    # TODO
    pit.buy_new_book(title='Ich bin dann mal weg', isbn='3-345-678')
    pit.buy_new_book(title='im Westen nichts neues', isbn='6-444-856')
    pit.buy_new_book(title='Das Omen', isbn='3-3345-678-X')
    pit.buy_new_book(title='Harry Potter, die neue Welt', isbn='3-4321-334')
    pit.buy_new_book(title='die schönsten Zugreisen', isbn='3-2123-554')
    library.print_inventory()

    # Ursula und Moritz leihen sich ein Buch aus
    # Teil 3
    # TODO
    ursula.borrow_a_book_by_title('Das Omen')
    moritz.borrow_a_book_by_title('Ich bin dann mal weg')
    library.print_inventory()

    # Ursula bringt ihr Buch zurück
    # Teil 4
    # TODO
    ursula.bring_back_a_book()
    library.print_inventory()

    # Moritz wird gemahnt
    # Teil 5
    # TODO
    pit.remind_customer('Moritz')
    library.print_inventory()

    # Pit löscht ein Buch aus der Bibliothek
    # TODO
    pit.remove_book('Harry Potter, die neue Welt')
    library.print_inventory()

    # Ursula will ein Buch, das es nicht gibt.
    # TODO
    pass


if __name__ == '__main__':
    main()

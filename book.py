from dataclasses import dataclass, field


@dataclass
class Book:
    """
    Die Klasse beschreibt ein Buch, das über seinen Titel und die ISBN-Nummer definiert ist.
    Die Informationen zum Buch können über get-Methoden abgefragt werden.

    Jedes Buch wird durch den Bibliothekar in der Bibliothek eingereiht. Dazu wird dem Buch
    der Ablageort bekannt gegeben.

    """

    '''
    Definition der Attribute.
    - title     Der Titel des Buchs
    - isbn      Die ISBN-Nummer des Buchs
    - location  Der Ablageort in der Bibliothek
    '''

    title: str
    isbn: str
    location: str = field(init=False)  # will be assigned by the librarian

    def __post_init__(self):
        self.location = None

    def print(self):
        """
        Gibt die Informationen des Buchs am Stdout aus.
        """
        print(f'ISBN : {self.isbn} / Titel: {self.title}  / Ablage : {self.location}')
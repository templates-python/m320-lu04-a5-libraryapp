from dataclasses import dataclass

@dataclass
class Book:
    '''
    Die Klasse beschreibt ein Buch, das über seinen Titel und die ISBN-Nummer definiert ist.
    Die Informationen zum Buch können über get-Methoden abgefragt werden.

    Jedes Buch wird durch den Bibliothekar in der Bibliothek eingereiht. Dazu wird dem Buch
    der Ablageort bekannt gegeben.

    Author  : René Probst
    Date    : 30.08.2022
    Version : 1.0
    Changed : 26.8.2023
    Version : 2.0   (Klasse als dataclass umgebaut)
    '''

    '''
    Definition der Attribute.
    - title     Der Titel des Buchs
    - isbn      Die ISBN-Nummer des Buchs
    - location  Der Ablageort in der Bibliothek
    '''

    title: str = None # wird durch den Aufruf des (impliziten) Konstruktors initialisiert
    isbn: str = None  # dito
    location: str = None # wird erst zur Laufzeit, wenn das Buch in der Bibliothek abgelegt wird, zugewiesen

    def print(self):
        '''
        Gibt die Informationen des Buchs am Stdout aus.
        '''
        print(f'ISBN : {self.isbn} / Titel: {self.title}  / Ablage : {self.location}')
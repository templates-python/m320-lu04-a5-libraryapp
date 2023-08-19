class Book:
    '''
    Die Klasse beschreibt ein Buch, das über seinen Titel und die ISBN-Nummer definiert ist.
    Die Informationen zum Buch können über get-Methoden abgefragt werden.

    Jedes Buch wird durch den Bibliothekar in der Bibliothek eingereiht. Dazu wird dem Buch
    der Ablageort bekannt gegeben.

    Author  : René Probst
    Date    : 30.08.2022
    Version : 1.0
    Changed : ...
    '''

    def __init__(self, title, isbn):
        '''
        Initialisiert ein Objekt vom Typ Buch mit dem Titel und der ISBN-Nummer.
        zu beachten: Das konkrete Buch weiss noch nicht, wo es in der Bibliothek eingetragen ist.
        Dies erfolgt erst über den Setter für location.
        :param title: Titel des Buchs
        :param isbn:  ISBN-Nummer des Buchs
        '''
        self._title = title
        self._isbn  = isbn
        self._location = None

    def print(self):
        '''
        Gibt die Informationen des Buchs am Stdout aus.
        '''
        print(f'ISBN : {self._isbn} / Titel: {self._title}  / Ablage : {self._location}')

    @property
    def title(self):
        '''
        Liest den Titel des Buchs aus.
        :return: Buchtitel
        '''
        return self._title

    @property
    def isbn(self):
        '''
        Liest die ISB-Nummer des Buchs aus
        :return: ISBN-Nummer
        '''
        return self._isbn

    @property
    def location(self):
        '''
        Liest den Ablageort des Buchs aus.
        :return: Ablageort
        '''
        return self._location

    @location.setter
    def location(self, location):
        '''
        Setzt den Ablageort des Buchs.
        :param location: Ablageort des Buchs
        '''
        self._location = location

    '''
    Für die Attribute title und isbn gibt es keine setter.
    Sie werden einmalig bei der Erzeugung des Programms geschrieben.
    '''


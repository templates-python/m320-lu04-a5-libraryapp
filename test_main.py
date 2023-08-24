import pytest
from main import main
import re

def test_main_part1(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Bibliotheks-Anwendung\n=====================\n\nKunden:\nKunde: Moritz\nKunde: Ursula\n---\n'

def test_main_part2(capsys):
    main()
    captured = capsys.readouterr()
    output = captured.out

    # Der erwartete reguläre Ausdruck
    expected_pattern = r'''Bibliotheks-Anwendung\n=====================\n\nKunden:\nKunde: Moritz\nKunde: Ursula\n---\nInventar:\nISBN : 3-345-678 / Titel: Ich bin dann mal weg  / Ablage : [A-Z][1-9]|10\nISBN : 6-444-856 / Titel: im Westen nichts neues  / Ablage : [A-Z][1-9]|10\nISBN : 3-3345-678-X / Titel: Das Omen  / Ablage : [A-Z][1-9]|10\nISBN : 3-4321-334 / Titel: Harry Potter, die neue Welt  / Ablage : [A-Z][1-9]|10\nISBN : 3-2123-554 / Titel: die schönsten Zugreisen  / Ablage : [A-Z][1-9]|10\n---'''

    # Überprüfung der Ausgabe mit dem regulären Ausdruck
    assert re.match(expected_pattern, output), f"Die Ausgabe entspricht nicht dem erwarteten Muster:\n {output}"

def test_main_part3(capsys):
    main()
    captured = capsys.readouterr()
    output = captured.out
    # den schon getesteten Teil aus dem output löschen (Teilstring)
    index = output.index('---')
    index = output.index('---', index+1)
    compared_string = output[index + len('---'):]

    # Der erwartete reguläre Ausdruck
    expected_pattern = r'''\nUrsula hat das Buch 'Das Omen' erhalten.\nMoritz hat das Buch 'Ich bin dann mal weg' erhalten.\nInventar:\nISBN: 6 - 444 - 856 / Titel: im Westen nichts neues / Ablage: [A-Z][1-9]|10\nISBN: 3 - 4321 - 334 / Titel: Harry Potter, die neue Welt / Ablage: [A-Z][1-9]|10\nISBN: 3 - 2123 - 554 / Titel: die schönsten Zugreisen / Ablage: [A-Z][1-9]|10\n---'''

    #INLINE TEST
    print(f'\nPATTERN:\n{expected_pattern}')
    print('***')
    print(f'\nOUTPUT :\n{compared_string}')
    #INLINE TEST
    # Überprüfung der Ausgabe mit dem regulären Ausdruck
    assert re.match(expected_pattern, compared_string), f"Die Ausgabe entspricht nicht dem erwarteten Muster:\n {compared_string}"


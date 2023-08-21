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
    expected_pattern = r'''Bibliotheks-Anwendung\n=====================\n
                           \n
                           Kunden:\n
                           Kunde: Moritz\n
                           Kunde: Ursula\n
                           ---\n
                           Inventar:\n
                           ISBN : 3-345-678 / Titel: Ich bin dann mal weg  / Ablage : [a-zA-Z0-9]{1,4}\n
                           ISBN : 6-444-856 / Titel: im Westen nichts neues  / Ablage : [a-zA-Z0-9]{1,4}\n
                           ISBN : 3-3345-678-X / Titel: Das Omen  / Ablage : [a-zA-Z0-9]{1,4}\n
                           ISBN : 3-4321-334 / Titel: Harry Potter, die neue Welt  / Ablage : [a-zA-Z0-9]{1,4}\n
                           ISBN : 3-2123-554 / Titel: die schönsten Zugreisen  / Ablage : [a-zA-Z0-9]{1,4}\n
                           ---\n'''


    # Überprüfung der Ausgabe mit dem regulären Ausdruck
    assert re.match(expected_pattern, output), f"Die Ausgabe entspricht nicht dem erwarteten Muster:\n {output}"
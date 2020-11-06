from core import foo		
"""Whole Funktion Foo aus Package Core"""

"""Name markiert Funktion als Testfunktion"""
def test_foo():			
    assert foo(2) == 3
"""Testet Funktion und schaut ob Funktion den richtigen Wert ausgibt"""


"""Ausführen des Tests in Python Konsole mit Programm pytest"""
def test_foo_two_args():
    assert foo(2,3) == 6
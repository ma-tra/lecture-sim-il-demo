from core import foo		"""Whole Funktion Foo aus Package Core"""

def test_foo():			"""Name markiert Funktion als Testfunktion"""
	assert foo(2) == 3 	"""Testet Funktio und schaut ob Funktion den richtigen Wert ausgibt"""

"""Ausführen des Tests in Python Konsole mit programm pytest"""

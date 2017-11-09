# EPR_Aufgabe_3


GitHub Readme:
https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf

Key Pressing
getch() <conio.h> : Diese Funktion ist defakto Standard und funktioniert ähnlich wie getchar(). Mit dem Unterschied, dass der Benutzer auch wirklich nur maximal ein Zeichen eingeben kann. Außerdem erzeugt getch() kein Echo auf der Konsole, d.H. der Benutzer sieht nicht was er eingibt (geeignet z.B. für kleine Spiele oder die Eingabe eines Passwortes). 

ord(c)
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the integer 97, ord(u'\u2020') returns 8224. This is the inverse of chr() for 8-bit strings and of unichr() for unicode objects. If a unicode argument is given and Python was built with UCS2 Unicode, then the character’s code point must be in the range [0..65535] inclusive; otherwise the string length is two, and a TypeError will be raised.

key = ord(getch())

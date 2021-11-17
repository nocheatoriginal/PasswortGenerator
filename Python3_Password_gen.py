'''
Generiert ein Passwort mit mindesten 4 Zeichen
und höchstens 20 Zeichen. Das Passwort kann Kleinbuchstaben,
Großbuchstaben, Zahlen und ausgewählte Sonderzeichen enthalten.
Das Passwort mit beliebiger Länge (20 <= Passwort >= 4) wird
in einer Text-Datei 'neues_passwort.txt' gespeichert und in die
Zwischenablage kopiert.
Passwortgenerator von nocheatoriginal

# TODO
Alle generierten Passwörter sollen in der gleichen Datei
gespeichert sein. User sollen eine Applikation oder Internet-
seite dazu schreiben lassen können, um in der Textdatei die
Passwörter für die jeweiligen Dienste zu finden.
'''
import random, os
from tkinter import Tk

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
all_symbols = "[]}{#()*;._-?!§$%&\"\\/'²³@|<>=+,:~" # Auch möglich...
symbols = "._-*!?<>"
allowed_characters = lower_case + upper_case + numbers + symbols

def generate(length): # Generiert das Passwort
    return "".join(random.sample(allowed_characters, length))

def isInt(value): # Wenn der Wert in eine Zahl konvertiert werden kann True, andernfalls False
    try:
        if int(value):
            return True
    except ValueError:
        return False
    
def consoleClear():
    try:
        clear = lambda: os.system('cls')
        clear()
    except:
        try:
            clear = lambda: os.system('clear')
            clear()
        except:
            clear = "FEHLER"

def main():
    while True:
        print("Empfohlene Passwortlänge: 12;\nMindestens 4; Höchstens 20;")

        user_input = input("Passwortlänge>>> ")
        while isInt(user_input) == False or int(user_input) < 4 or int(user_input) > 20:
            consoleClear()
            print(f"Empfohlene Passwortlänge: 12;\nMindestens 4; Höchstens 20;")
            user_input = input("Passwortlänge>>> ")
        
        successfully = False

        try:
            passwort = generate(int(user_input))
            print(f"Passwort:{passwort}")
            successfully = True
        except:
            print(f"{user_input = }: falsche Eingabe!")
            successfully = False

        if successfully:
            request_save = input("In Zweischenablage kopieren und das\nPasswort in einer Datei speichern? [J/n] ")
            if request_save == 'JA' or request_save == 'Ja' or request_save == 'ja' or request_save == 'J' or request_save == 'j' or request_save == '':
                with open("neues_passwort.txt", "w") as save_file:
                    save_file.write("PASSWORT:%s" % passwort)

                    clipboard = Tk()
                    clipboard.withdraw()
                    clipboard.clipboard_clear()
                    clipboard.clipboard_append(passwort)
                    clipboard.update()
                    
                    input("Erledigt!\nMit Eingabetaste das Programm beenden ...")
                return False
            else:
                consoleClear()

if __name__ == '__main__':
    main()

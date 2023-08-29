# 1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
# caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
# preluat automat de la tastatura.

string = input('Introdu caractere: ')
name = input('Introdu numele tău: ')
print(f'Șirul de {"litere" if string.isalpha() else "cifre" if string.isdecimal() else "caractere"} '
      f'a fost găsit de {name}.')

# 2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.

print('The number is ' + ('odd.' if int(input('Enter a number: ')) % 2 else 'even.'))


# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest)

def is_leap_year(year):
    return False if year % 4 else True if year % 100 else False if year % 400 else True


print('It is ' + ('' if is_leap_year(int(input('Enter year: '))) else 'not ') + 'a leap year.')


# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.

def sign(n):
    return -n if n < 0 else 'Numărul este 0' if n == 0 else 'Numărul e <10' if n < 10 else n


print(sign(int(input('Enter a number: '))))


# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
# acest sir de caractere:
# “”” 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”

menu = ['Alegerea nu exista. Reincercati.', 'Afisare lista de cumparaturi', 'Adaugare element',
        'Stergere element', 'Sterere lista de cumparaturi', 'Cautare in lista de cumparaturi']

for i in range(1, len(menu)):
    print(f'{i} - {menu[i]}')

choice = int(input('\nIntrodu un număr între 1 și 5: '))
print(menu[choice] if choice in range(1, 6) else menu[0])

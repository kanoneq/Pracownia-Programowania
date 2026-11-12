#te funkcje i 27 linijka sa na tyle zlozone ze nie wydaje mi sie ze bym mogl je wytlumaczyc w formie pisemnej, wiec jesli ktos by chcial, to moze do mnie napisac i wtedy postaram sie wytlumaczyc
def poimionach(uczen):
  return uczen['imie'];

def poocenach(uczen):
  return uczen['ocena'];
#tez dodam ze na lekcji zamiast "uczen" bylo "e", ale zmienilem to dla wygody i przejrzystosci kodu

#tablica w formacie: ['imie': 'Franek', 'ocena': 3] dla przykladu oznacza ze tworzymy jeden obiekt w tablicy ktory posiada zmienna imie o wartosci Franek i zmienna ocena o wartosci 3
uczniowie = [
  {'imie': 'Soffia', 'ocena': 1},
  {'imie': 'Dawid', 'ocena': 4},
  {'imie': 'Pawel', 'ocena': 2},
  {'imie': 'Kinga', 'ocena': 1},
  {'imie': 'Franek', 'ocena': 3},
  {'imie': 'Ania', 'ocena': 5},
  {'imie': 'Damian', 'ocena': 2},
  {'imie': 'Adrian', 'ocena': 6},
]

#tworzenie inputa zeby zastosowac if'y w zadaniu
input = input("wpisz 1 lub 2 teraz: ");


#jesli user wpisze 1 to sortujemy po imionach, jesli 2 to sortujemy po ocenach a jesli cos innego to oddajemy wiadomosc ze input jest niepoprawny
if input == "1":
    uczniowie.sort(key=poimionach);
    print("posortowane po imionach: ");
    print(uczniowie);
elif input == "2":
    uczniowie.sort(key=poocenach);
    print("posortowane po ocenach: ");
    print(uczniowie);
else:
    print("niepoprawny input, prosze wpisac 1 lub 2");
#ten kod wpisal "text do pliku" do pliku koszula.txt w tym folderze
# with open("koszula.txt", "a") as f:
#     f.write("text w pliku")

#zdefiniowanie zmiennych ktore tworza strukture pliku xml
zawartosc1 = """<?xml version="1.0" encoding="UTF-8"?>
<pupil>
    <imie>"""
zawartosc2 = """</imie>
    <waga>"""
zawartosc3 = """</waga>
    <rasa>"""
zawartosc4 = """</rasa>
</pupil>"""

#pytanie o zmienne ktore beda wykorzystane jako wartosc
zmienna_imie=input("wpisz imie pupila: ")
zmienna_waga=input("wpisz wage pupila (w kg): ")
zmienna_rasa=input("wpisz rase pupila: ")

#sklejanie klockow struktury z zmiennymi wzietymi od usera
full_zawartosc = zawartosc1 + zmienna_imie + zawartosc2 + zmienna_waga + zawartosc3 + zmienna_rasa + zawartosc4


#wpisanie sklejonej calosci do pliku "plikxml.xml"
with open("plikxml.xml", "w") as file:
    file.write(full_zawartosc)

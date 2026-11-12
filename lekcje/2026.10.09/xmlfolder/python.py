#to otwiera plik (w tym przypadku plik.xml) w trybie odczytu (r)
file = open("plik.xml", "r", encoding="UTF-8")

#odczytujemy otwarty wczesniej plik
odczytany_plik = file.read()

print(odczytany_plik)

#zamykamy plik po zakonczeniu operacji nad nim
file.close()
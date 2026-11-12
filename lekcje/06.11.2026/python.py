import random

#randomowe wybieranie liczby hexadecymalnej, 2**24 to maksymalna liczba hex ktora sie zawiera w 6 cyfrach, tyle ile potrzeba do oznaczenia koloru
kolor = hex(random.randrange(0, 2**24))
#uzywanie funkcji "hex" w pythonie sprawia ze liczby szesnastkowe sie zaczynaja zawsze na "0x", linijka ponizej wywala to z tej liczby
bez_zerox = kolor[2:]
#tutaj dodajemy # do poczatku liczby, bo tylko wtedy zostanie to przyjete jako valid color w CSS'sie (tak mi sie wydaje, moze to dzialac bez, nie sprawdzalem)
pelny_hex = "#" + bez_zerox

#sklejanie CSS'a tak jak to robilismy za 1 razem z XMLem
pierwsza_czesc_css = (
"""
*{
    background-color: """)

druga_czesc_css = (
"""
}
"""
)
caly_css = pierwsza_czesc_css + pelny_hex + ";" + druga_czesc_css

#zapisanie do pliku CSS'a
with open("kolor.css", "w") as cssfile:
    cssfile.write(caly_css)
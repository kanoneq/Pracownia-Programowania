import xml.etree.ElementTree as ET

#caly kod jest w funkcji bo tak na jakiejs stronie bylo napisane
def GenerateXML(fileName):
    root = ET.Element("osoby")
    #nadanie atrybutu ID o wartosci 0 dla roota
    root.set("ID", "0")

    osoby = ["osoba1", "osoba2", "osoba3", "osoba4", "osoba5"]

    for osoba in osoby:
        #stworzenie na poczatku kontenera osoby (nazwa zalezna od iteracji loopa)
        SE=ET.SubElement(root, osoba)
        #branie z klawiatury wszystkich ocen
        ocena_polski=int(input("podaj ocene z polskiego dla " + osoba + ": "))
        ocena_matma=int(input("podaj ocene z matmy dla " + osoba + ": "))
        ocena_angielski=int(input("podaj ocene z angielskiego dla " + osoba + ": "))
        ocena_wf=int(input("podaj ocene z wfu dla " + osoba + ": "))
        ocena_religia=int(input("podaj ocene z religii dla " + osoba + ": "))
        #obliczanie sredniej i printowanie czy jest pasek
        srednia: float = (ocena_polski + ocena_matma + ocena_angielski + ocena_wf + ocena_religia)/5
        
        #zamiana wszystkich ocen spowroten na stringi (xml nie przyjmuje innych zmiennych)
        ocena_polski=str(ocena_polski)
        ocena_matma=str(ocena_matma)
        ocena_angielski=str(ocena_angielski)
        ocena_wf=str(ocena_wf)
        ocena_religia=str(ocena_religia)
        srednia=str(srednia)

        SSE=ET.SubElement(SE, "ocena_polski")
        SSE.text = ocena_polski
        SSE=ET.SubElement(SE, "ocena_matma")
        SSE.text = ocena_matma
        SSE=ET.SubElement(SE, "ocena_angielski")
        SSE.text = ocena_angielski
        SSE=ET.SubElement(SE, "ocena_wf")
        SSE.text = ocena_wf
        SSE=ET.SubElement(SE, "ocena_religia")
        SSE.text = ocena_religia
        SSE=ET.SubElement(SE, "srednia")
        SSE.text = srednia

        #zamiana sredniej spowrotem na int zeby if mogl poprawnie ja sprawdzic, przenioslem ten kod tutaj zeby ladniej w XMLu wygaldalo
        srednia = float(srednia)

        #ten if robi kilka rzeczy, zaleznie od sredniej wypisuje w terminalu i dodaje kolejny element w xml'u z dana czy jest pasek czy nie ma
        if srednia > 4.75:
            string = "pasek na swiadectwie dla " + osoba
            print(string)
            SSE=ET.SubElement(SE, "czy_pasek")
            SSE.text = string
        else:
            string = "pasek na dupie dla " + osoba
            print(string)
            SSE=ET.SubElement(SE, "czy_pasek")
            SSE.text = string


    #sklejenie wszystkiego w jedno drzewo
    tree = ET.ElementTree(root)
    #dla estetyki (\t oznacza taba)
    ET.indent(tree, space="\t")
    #nadpisanie/stworzenie pliku xml ze wszystkimi ocenami i srednimi
    with open(fileName, "wb") as files:
        tree.write(files, encoding="utf-8", xml_declaration=True) #to dodaje ta pierwsza linijke z encodingiem itd.

#wywolanie funkcji (calego kodu tak naprawde) i nadanie plikowi nazwe
GenerateXML("plik_drugi.xml")
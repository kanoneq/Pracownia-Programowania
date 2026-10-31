import xml.etree.ElementTree as ET

#ten plik tworzy plik .xml i dodaje wartosci do dwoch obiektow

pierwsza_zmienna = input("podaj wartosc 1 obiektu: ")
druga_zmienna = input("podaj wartosc 2 obiektu: ")


def GenerateXML(fileName):
    root=ET.Element("root")

    O1=ET.Element("pierwszy_tab")
    root.append(O1)

    SE1=ET.SubElement(O1, "pierwszy_obiekt")
    SE1.text = pierwsza_zmienna

    SE2=ET.SubElement(O1, "drugi_obiekt")
    SE2.text = druga_zmienna


    tree = ET.ElementTree(root)

    ET.indent(tree, space="\t")

    with open(fileName, "wb") as files:
        tree.write(files, encoding="utf-8", xml_declaration=True)

GenerateXML("Nazwa_pliku.xml")
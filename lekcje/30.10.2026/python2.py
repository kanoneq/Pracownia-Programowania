import xml.etree.ElementTree as ET


def GenerateXML(fileName):
    root = ET.Element("osoby")

    osoby = ["osoba1", "osoba2", "osoba3", "osoba4", "osoba5"]

    for osoba in osoby:
        SE=ET.SubElement(root, osoba)
        ocena_polski=int(input("podaj ocene z polskiego dla " + osoba + ": "))
        ocena_matma=int(input("podaj ocene z matmy dla " + osoba + ": "))
        ocena_angielski=int(input("podaj ocene z angielskiego dla " + osoba + ": "))
        ocena_wf=int(input("podaj ocene z wfu dla " + osoba + ": "))
        ocena_religia=int(input("podaj ocene z religii dla " + osoba + ": "))
        srednia = (ocena_polski + ocena_matma + ocena_angielski + ocena_wf + ocena_religia)/5
        if srednia > 4.75:
            print("Pasek na swiadectwie")
        else:
            print("pasek na dupie")
        
        
        ocena_polski=str(ocena_polski)
        ocena_matma=str(ocena_matma)
        ocena_angielski=str(ocena_angielski)
        ocena_wf=str(ocena_wf)
        ocena_religia=str(ocena_religia)

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



    tree = ET.ElementTree(root)

    ET.indent(tree, space="\t")

    with open(fileName, "wb") as files:
        tree.write(files, encoding="utf-8", xml_declaration=True)

GenerateXML("plik.xml")
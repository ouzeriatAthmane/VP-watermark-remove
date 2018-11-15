import os
import errno
import glob

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


listeFichier = glob.glob("./Entrer/*.svg")
if len(listeFichier) > 0:
    print("Suppression logo de : \n")
else:
    print("Pas de fichier svg en Entrer")

for fichier in listeFichier:
    monFicher = open(fichier, "r")
    tmpSting = monFicher.read()
    monFicher.close
    tmpSting = tmpSting.replace(
        "Visual Paradigm Enterprise [evaluation copy] ", "")
    nomSortie = fichier[9:]
    print(nomSortie)
    createFolder('./Sortie/')
    f = open("./Sortie/"+nomSortie, "w+")
    f.write(tmpSting)
    f.close

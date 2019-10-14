# -*-coding:utf-8 -*

#la ligne ci-dessus permet de préciser le type d'encodage

from liste_nom import nom
import os
#le import os permet d'importer le module os qui dispose de variables et de fonctions utiles pour dialoguer avec le système d'exploitation

def imprime():
    for value in nom.values():
    #for key in nom:
    #   print (key) //ici on a les pays
        print (value) #ici on imprime les noms des personnes

    for key,value in nom.items():
       print (key+" "+value)  #//ici on imprime les deux


    print (nom["Angola"])
    
if __name__=="__main__":
    imprime()
    os.system("pause")
    
#le bout de code ci-dessus met le code en pause lorsqu'on exécute le fichier en double cliquant dessus et permet de voir le résultat de la fonction 'imprime' avant que la fenêtre se referme


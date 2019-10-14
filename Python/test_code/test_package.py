from packagetest.fonctions import table, verif_chiffre

try:
    chiffre=int(input("donnez un chiffre entier"))
    table(chiffre)
#les inputs renvoient toujours du type string du coup si on a besoin de chiffre il faut les convertir mais attention car si l'utilisateur n'écrit pas un chiffre convertible en int le programme plante

except ValueError:
    print("Variable incompatible avec un entier")
    
#print(verif_chiffre("bb"))


#test de mettre la vérification try et except dans une fonction
verif=False

while verif==False:
    chiffre=input("donnez un chiffre entier")
    verif=verif_chiffre(chiffre)
    
monchif=int(chiffre)
print(monchif)
from package import mesfonctions

print(mesfonctions.afficher_flottant(3.999999))

partie_entiere,reste=mesfonctions.decomposer(20,3)
print(partie_entiere,"et",reste)

mesfonctions.mafonction(2,3,5)
mesfonctions.mafonction('a','b')

mesfonctions.mafonction_deux('Patrizia','Battisti','comm','comm')

mesfonctions.afficher("Je suis une phrase","je suis une deuxième phrase")

uneliste=[0,1,2,3,4,5]
liste2=[nb*nb for nb in uneliste] #permet de parcourir une liste et de la modifier en une ligne

print(uneliste)
print(liste2)

# exercice de tri d'un inventaire
inventaires=[("pomme",22),("melon",4),("poire",18),("fraise",76),("prune",51)]
inv2=[]
[inv2.append((fruit[1],fruit[0]))for fruit in inventaires]
inv2.sort()
inv2.reverse()
inv3=[]
[inv3.append((fruit[1],fruit[0]))for fruit in inv2]
print(inv3)

#correction en 3 lignes -,-
inventaire_inverse=[(qtt,nom_fruit) for nom_fruit,qtt in inventaires]

inventaire_inverse.sort(reverse=True)
inventaires=[(nom_fruit,qtt) for qtt,nom_fruit in inventaire_inverse]

# ou encore en 1 ligne, on peut également mettre des conditions dans les compréhensions(ce sont les for en 1 ligne)
inventaires=[(nom_fruit,qtt) for qtt,nom_fruit in sorted(inventaire_inverse,reverse=True)]

print(inventaires)

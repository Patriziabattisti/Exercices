from packagetest.fonctions import verif_gagnant, roulette, verif_chiffre

from math import ceil

jouer=True
monargent=1000
nbjoueur=-1
misejoueur=0

while monargent>0 and jouer==True:
    chiffre_gagnant=roulette()
    #print(chiffre_gagnant)
    
    #nbjoueur=int(input("Choisissez un chiffre entre 0 et 49: "))
    #vérification que ce soit bien un entier sinon pas de conversion en int
    while nbjoueur<0 or nbjoueur>49:
        nbjoueur=input("Choisissez un chiffre entre 0 et 49: ")
        
        try:
            nbjoueur=int(nbjoueur)
        except ValueError:
            print("ce n'est pas un chiffre!")
            nbjoueur=-1
            continue
        if nbjoueur<0:
            print("nombre négatif!")
        if nbjoueur>49:
            print("ce nombre est supérieur à 49!")
    
    
    #misejoueur=int(input('quelle est votre mise ? '))
    #ici deux vérifications 1) que la mise ne soit pas plus grande que mon total et pas en négatif ou zéro
    #2) que ce soit bien un chiffre sinon pas de conversion en int
    while misejoueur<=0 or misejoueur>monargent:
        misejoueur=input('quelle est votre mise ? ')
        
        try:
            misejoueur=int(misejoueur)
        except ValueError:
            print("ce n'est pas une mise!")
            misejoueur=0
            continue
        if misejoueur<=0:
            print("mise négative!!")
        if misejoueur>monargent:
            print("vous ne pouvez pas miser plus que ce que vous avez!")
    
    
    monargent-=misejoueur
    
    result=verif_gagnant(chiffre_gagnant,nbjoueur)
    
    if result==1:
        monargent+=3*misejoueur
    elif result==2:
        monargent+=ceil(misejoueur/2)
    
    #demande à l'utilisateur s'il veut continuer pour lui permettre de sortir du jeu avec son argent ;)
    print ("il vous reste ",monargent, " euros")  
    contin=input("Voulez-vous continuez à jouer (o/n)?")
    
    if contin=="n":
        jouer=False
        print("au revoir")
    print("-------------------------------------------")
        
    
    




from random import randrange, randint

def table(nb, max=10):
    i=0
    while i<max:
        print(i+1,"*",nb,"=",(i+1)*nb)
        i+=1
        
def verif_chiffre(var):
    verif=True
    
    try:
        int(var)
        
    except ValueError:
        
        print("Variable incompatible avec un entier")
        verif=False
        
    return verif

def roulette():
    
    gagnant=randrange(50)
    
    return gagnant

def couleur(nb):
    
    if nb%2==0:
        macoul='black'
    else:
        macoul='red'
        
    return macoul

def verif_gagnant(nbbon,nbjoueur):
    if(nbbon==nbjoueur):
        print("bravo vous avez gagnez")
        return 1
    elif (couleur(nbbon)==couleur(nbjoueur)):
        print("c'est la bonne couleur")
        return 2
    else:
        print("perduuuu")
        return 3
#fonction pour renvoyer un float en string en deux parties avec 3 chiffres derrière la virgule
def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError("Le paramètre doit être un float")
    flottant=str(flottant)
    partie_entiere,partie_flottante=flottant.split(".")
    #la partie flottante doit être troncquée pour ne donner que 3 chiffres derrière la virgule
    
    return ",".join([partie_entiere,partie_flottante[:3]])

#--------------------------------------------------
#fonction qui retourne la partie entière et le reste d'un entier diviser par un nombre
def decomposer(entier,divise_par):
    
    # la division avec // permet d'avoir la partie entière de la division
    p_e=entier//divise_par
    
    # le modulo % permet d'avoir le reste de la division
    reste=entier%divise_par
    
    return p_e,reste #on retourne deux nombres
#----------------------------------------------------------------
#fonction dont on ne connait pas le nombre de paramètre à l'avance ! ne marche pas avec les paramètres nommés

def mafonction(*param):
    print("J'ai reçu ces paramètres: {}.".format(param))
    
#si maintenant on veut mettre des paramètres nommés, il faut les mettre avant
def mafonction_deux(nom,prenom,*comm):
    print("Voici mon nom et mon prénom: {} {}".format(nom,prenom))
    print("J'ai reçu ces paramètres: {}.".format(comm))
#----------------------------------------------------------------

#fonction pour afficher du texte comme print
def afficher(*valeurs,sep=' ', fin='\n'):
    #on récupère la chaine de caractère, phrase ou mots et on les place dans une liste
    mesmots=list(valeurs)
    
    #on parcourt la liste et on change chaque valeur en string
    for i,val in enumerate(mesmots):
        mesmots[i]=str(val)
     
    #on prend chaque partie et on construit une seule longue string avec le séparateur choisit
    chaine=sep.join(mesmots)
    #on finit la string avec un retour à la ligne
    chaine+=fin
    
    print(chaine)
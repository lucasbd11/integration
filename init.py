
def integrate(fonc,a,b,num_points):
    """
    Prend en entrée une fonction, ainsi que 2 réels et 1 entier naturel qui représentent dans l'ordre:
    a = le borne inférieur
    b = la borne supérieure
    num_points = le nombre de points (qui défini la taille des intervalles) utilisés pour calculer l'intégrale.
    La fonction renvoie un réel qui correspond au calcul de l'intégrale.
    """
    
    sum_1 = 0 # on initialise les 2 variables utilisés pour faire la méthode des trapèzes.
    sum_2 = 0
    
    base_width = (b-a)/num_points #on crée la variable qui contient la largeur d'une base.
    
    for i in range(num_points): #boucle pour calculer l'intégrale
        sum_1 += fonc((i)*base_width)*base_width
        sum_2 += fonc((i+1)*base_width)*base_width
    
    
    return (sum_1+sum_2)/2 #on renvoie la moyenne des 2 sommes.


fct = lambda x: 4*x #test avec une fonction linéaire.


value = integrate(fct,0,10,10000)

from random import randint

def jeu_des(j1,j2):
    print('Le joueur faisant le plus haut score en lançant un dé gagne!')
    des=jeu(j1,j2)
    de1=des[0]
    de2=des[1]
    g=gagnant(j1,j2,de1,de2)
    j_g=g[0]
    k=g[1]
    return j_g,k

def jeu(j1,j2):
    print()
    print(j1,'vous commencez :')
    dé=input("Appuyez sur entrée pour lancer le dé")
    de1=randint(1,6)
    print('Vous avez fait',de1)
    print()
    print(j2,'à votre tour')
    dé=input("Appuyez sur entrée pour lancer le dé")
    de2=randint(1,6)
    print('Vous avez fait',de2)
    return de1,de2

def gagnant(j1,j2,de1,de2):
    k=1
    if de1==de2:
        while de1==de2:
            des=jeu(j1,j2)
            de1=des[0]
            de2=des[1]
            k+=1
    if de1>de2:
        j_g=j1
    if de1<de2:
        j_g=j2
    return j_g,k
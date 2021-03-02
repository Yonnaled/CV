from render_connect4 import *

def p4():
    """
    """
    nr_=6
    nc_=7
    init=initialisation_p4(nr_,nc_)
    g=init[0]
    d_g=init[1]
    
    
    draw_connect4(g)
    fini="non"
    player=1
    k=0
    while fini!="oui":
        
        
        lc=joue_coup(g,d_g,player,nr_,nc_)
        if is_align4(g,lc,player)==True:
            fini="oui"
            joueur_gagnant=player
            print("Partie finie")
        
        
        draw_connect4(g)
        
        k+=1
        if k == nc_*nr_:
            fini="oui"
            joueur_gagnant=0
            print("Partie finie")

        if player==1:
            player=2
        else:
            player=1
    
    return joueur_gagnant
    wait_quit()

def initialisation_p4(nr,nc):
    """
    initialise une grille de jeu de nr lignes et nc colonnes, et qui ne contient aucun disque.
    """
    d_g=[[k] for k in range(nc)]
    grille=[]
    for i in range(nr):
        grille+=[[0]*nc]
    for k in range(nc):
        d_g[k]={k:0}
        d_g[k]["jouable"]='oui'
    return [grille,d_g]
    
def nr(g):
    """
    donne le nb de lignes de la grille g
    """
    return len(g)

def nc(g):
    """
    donne le nb de colonnes de la grille g
    """
    return len(g[0])

#def affiche_g_1(g):
#    """
#    """
#    nc_=nc(g)
#    nr_=nr(g)
#    if nc_<11:
#        for i in range(nr_):
#            for k in range(nc_):
#                if k==nc_-1:
#                    if g[i][k]==0:
#                        print('-')
#                    elif g[i][k]==2:
#                        print('X')
#                    elif g[i][k]==1:
#                        print('O')
#                else:
#                    if g[i][k]==0:
#                        print('-',end='')
#                    elif g[i][k]==2:
#                        print('X',end='')
#                    elif g[i][k]==1:
#                        print('O',end='')
#        print("="*nc_)
#        for i in range(nc_):
#            print(i,end='')
#        print()
    
def joue_coup(g,d_g,player,nr_,nc_):
    """
    """
    for d in range(len(d_g)):
            if d_g[d][d]==nr_:
                d_g[d]["jouable"]="non"
    
    col_ok="non"
    colonne=0
    while col_ok!="oui":
        col=input("Colonne à jouer? :  ")
        try:
            colonne=int(col)
            assert colonne<nc_ and colonne>=0
            assert d_g[colonne]["jouable"]=="oui"
        except ValueError:
            print("Entrez un chiffre")
        except AssertionError:
            print("Entrez une colonne jouable")
        except IndexError:
            print("Entrez une colonne jouable")
        else:
            col_ok="oui"
            colonne=int(col)
    
    for l in reversed(g):
        if l[colonne]==0:
            if player==1:
                l[colonne]=1
            else:
                l[colonne]=2
            d_g[colonne][colonne]+=1
            
            lc_r=[]
            lc_d1=[]
            lc_d2=[]
            lc_c=[]
            g_reversed=list(g)
            g_reversed.reverse()
            for i in range(-3,4):
                lc_r+=[(g_reversed.index(l),colonne+i)]
                lc_c+=[(g_reversed.index(l)+i,colonne)]
                lc_d1+=[(g_reversed.index(l)+i,colonne+i)]
                lc_d2+=[(g_reversed.index(l)+i,colonne-i)]
            
            break
    return [lc_r,lc_d1,lc_d2,lc_c]
    

def is_align4(g,lc,p):
    """
    indique, pour la grille g, s’il y a 4 cases consécutives de valeur p pour les cases dont les coordonnées sont données dans la liste lc
    """
    g_reversed=list(g)
    g_reversed.reverse()
    for LC in lc:
        k=0
        res=False
        for i in range(6):
            try:
                g_reversed[LC[i][0]][LC[i][1]]==p
                assert LC[i][0]>=0 and LC[i][1]>=0
            except IndexError:
                k=0
            except AssertionError:
                k=0
            else:
                if g_reversed[LC[i][0]][LC[i][1]]==p:
                    k+=1
                    if k==4:
                        res=True
                        break
                else:
                    k=0
        if k==4:
            break
    return res




def is_win(g,r,c,p):
    """
    indique si la case (r,c) provoque la victoire du joueur p
    """
    pass


    

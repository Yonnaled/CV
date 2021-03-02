def morpion():
    """
    """
    p=1
    ini=init()
    g=ini[0]
    g_poss=ini[1]
    affiche_m(g)
    
    fini="non"
    tour=0
    while fini !='oui':
        joue_m(g,p)
        print('\n'*10)
        affiche_m(g)
        if coup_gagnant(g,g_poss,p)==True:
            print("Le joueur",p,"remporte la partie")
            fini='oui'
            joueur_gagnant=p
        
        
        if p==1:
            p=2
        else:
            p=1
        tour+=1
        if tour==9:
            joueur_gagnant=0
            print("Partie nulle")
            fini='oui'
            
    return joueur_gagnant
            
def init():
    g=[]
    for k in range(3):
        g+=[['0']*3]
    
    l1=[(0,0),(0,1),(0,2)]
    l2=[(1,0),(1,1),(1,2)]
    l3=[(2,0),(2,1),(2,2)]
    c1=[(0,0),(1,0),(2,0)]
    c2=[(0,1),(1,1),(2,1)]
    c3=[(0,2),(1,2),(2,2)]
    d1=[(0,0),(1,1),(2,2)]
    d2=[(0,2),(1,1),(2,0)]
    gagnant_possible=[l1,l2,l3,c1,c2,c3,d1,d2]
    return [g,gagnant_possible]

def affiche_m(g):
    g2=[[g[0][0],'|',g[0][1],'|',g[0][2]],['-']*11,[g[1][0],'|',g[1][1],'|',g[1][2]],['-']*11,[g[2][0],'|',g[2][1],'|',g[2][2]]]
        

    l1=g2[0]
    print('1 ¦',end='  ')
    for c in l1:
        if c=='0':
            print('  ',end=' ')
        elif c=='1':
            print(' X',end=' ')
        elif c=='2':
            print(' O', end=' ')
        else:
            print(c,end='')
    print()
    
    l2=g2[1]
    print('- ¦',end='  ')
    for c in l2:    
        print(c,end='')
    print()
    
    l3=g2[2]
    print('2 ¦',end='  ')
    for c in l3:
        if c=='0':
            print('  ',end=' ')
        elif c=='1':
            print(' X',end=' ')
        elif c=='2':
            print(' O', end=' ')
        else:
            print(c,end='')
    print()
    
    l4=g2[3]
    print('- ¦',end='  ')
    for c in l4:    
        print(c,end='')
    print()
    
    l5=g2[4]
    print('3 ¦',end='  ')
    for c in l5:
        if c=='0':
            print('  ',end=' ')
        elif c=='1':
            print(' X',end=' ')
        elif c=='2':
            print(' O', end=' ')
        else:
            print(c,end='')
    print()
    print('  ¦')
    print('-'*18)
    print('  ¦   1 | 2 | 3')

def joue_m(g,p):
    """
    """
    print()
    if p==1:
        print("Tour du joueur 1 :")
    else:
        print("Tour du joueur 2 :")
    case_choisie='non'
    while case_choisie!='oui':
        colonne=input('Colonne :  ')
        ligne=input('Ligne :  ')
        try:
            assert g[int(ligne)-1][int(colonne)-1]=='0'
            assert int(ligne)>0 and int(colonne)>0
        except AssertionError:
            print('Vous ne pouvez pas jouer cette case')
        except IndexError:
            print('Vous ne pouvez pas jouer cette case')
        except ValueError:
            print("Entrez des chiffres")
        else:
            case_choisie='oui'
            
    for c in g[int(ligne)-1]:
        if c==g[int(ligne)-1][int(colonne)-1]:
            if p==1:
                g[int(ligne)-1][int(colonne)-1]='1'
            if p==2:
                g[int(ligne)-1][int(colonne)-1]='2'

def coup_gagnant(g,g_poss,p):
    """
    """
    for c in g_poss:
        k=0
        for t in c:
            if p==1:
                if g[t[0]][t[1]]=='1':
                    k+=1
                    if k==3:
                        return True
                else:
                    k=0
            elif p==2:
                if g[t[0]][t[1]]=='2':
                    k+=1
                    if k==3:
                        return True
                else:
                    k=0
    return False

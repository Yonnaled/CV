
from random import randint
from interface import *
from puissance4 import *
from morpion import *
from jeu_des import * 
import copy
from random import shuffle

def jeu():
    """
    lance le jeu mario party, dans lequel on peut jouer à de smini-jeux comme le puissance 4, le morpion, etc...
    """
    nb_joueurs=nb_jrs()
    
    pseudo_et_liste=pseudos_jrs(nb_joueurs)
    pseudos_joueurs=pseudo_et_liste[0]
    liste_joueurs=pseudo_et_liste[1]
    
    init=initialisation(liste_joueurs,nb_joueurs)
    tours=init[0]
    plateau=init[1]
    etoile=init[2]
    prix_etoile=init[3]
    
    liste_obj=["vol 5pcs adv","vol 1 etoile adv","+3 son dé","-3 dé adv"]
    liste_mini_jeux=["p4","dés","morpion"]
    
    creation(plateau,liste_joueurs,etoile)
    
    tour=0
    while tour<(int(tours)*nb_joueurs):
        if tour%(2*nb_joueurs)==0 and tour!=0:
            if nb_joueurs>1:
                mini_jeux(liste_mini_jeux,pseudos_joueurs,liste_joueurs)
        j=tour%nb_joueurs
        print(liste_joueurs[j]["pseudo"],end=' ')
        begin=input("appuyez sur Entree pour commencer votre tour")
        clear_shell()
        objets(liste_joueurs,j,pseudos_joueurs,nb_joueurs,liste_obj)
        etoile=avancer(liste_joueurs,plateau,etoile,prix_etoile,j,liste_obj)
        liste_joueurs[j]["dé"]=6
        d=6   
        tour+=1
    etoiles_bonus(liste_joueurs)
    gagne=gagnant(liste_joueurs,nb_joueurs)
    fichier(liste_joueurs,tours,gagne)


def nb_jrs():
    """
    retourne le nombre de personnes voulant jouer au jeu
    :param return: (int) nombre de joueurs 
    """
    while True:
        nb_j=input("Nombre de joueurs? :  ")
        try:
            int(nb_j)
            assert int(nb_j)<5 and int(nb_j)>1
            return int(nb_j)
        except ValueError:
            print("Entrez un chiffre")
        except AssertionError:
            print("Le nombre de joueurs doit être compris entre 2 et 4")




def pseudos_jrs(nb_joueurs):
    """
    retourne la liste des pseudos des joueurs et une liste de dictionnaires comportant des informations sur chaque joueur.
    :param nb_joueurs: (int) nb de joueurs devant choisir leurs pseudos dans la fonction
    :param pseudos_joueurs: (list) liste des pseudos des joueurs
    :param liste_joueurs: (list) liste de dictionnaires comportant des informations sur les joueurs
    CU: type(nb_joueurs)==<class 'int'>
    """
    pseudos_joueurs=list(i for i in range(nb_joueurs))
    for i in range(nb_joueurs):
        choix_pseudo_fait='non'
        while choix_pseudo_fait!='oui':
            print("Pseudo du joueur n°",i+1,":  ")
            pseudos_joueurs[i]=input()
            try:
                assert pseudos_joueurs[i]!='!'
            except AssertionError:
                print("Pseudo inutilisable")
            else:
                choix_pseudo_fait='oui'
    print("Les joueurs sont :")
    for pseudo in pseudos_joueurs:
        print('  ',pseudo)
        
    liste_joueurs=[]
    d={"pseudo":"","position":0,"pieces":0,"etoiles":0,"objets":[],"dé":6,"nb_obj_tot":0,"nb_cases_tot":0,"nb_win_tot":0}
    
    for i in range(nb_joueurs):
        liste_joueurs+=[copy.deepcopy(d)]
    for i in range(nb_joueurs):
        liste_joueurs[i]["pseudo"]=pseudos_joueurs[i]
    return [pseudos_joueurs,liste_joueurs]

def creation(plateau,liste_joueurs,etoile):
    '''
    affiche le plateau de jeu
    :param plateau: (list) liste comprenant des 1, 2 et 3 pour créer le plateau
    :param liste_joueurs: (list) liste de dictionnaires comportant la clé "pieces"
    :param etoile: (int) indice de la place de l'etoile dans la liste plateau
    CU: type(etoile)==<class 'int'>
    '''
    cree_plateau(plateau)
    cree_perso(liste_joueurs,plateau)
    place_etoile(etoile,plateau)

def initialisation(liste_joueurs,nb_joueurs):
    """
    retourne le nombre de tours joués choisis par les joueurs, un plateau aléatoire, une position aléatoire de l'étoile, et le prix de  l'étoile.
    :param liste_joueurs: (list)
    :param nb_joueurs: (int)
    :param tours: (int)
    :param plateau: (list)
    :param etoile: (int)
    :param prix_etoile: (int)
    CU: "pieces" in d for d in liste_joueurs
    """
    nb_tours_accept="non"
    while nb_tours_accept!="oui":
        tours=input("Combien de tours voulez-vous jouer ? :  ")
        try:
            int(tours)
        except ValueError:
            print("Entrez un chiffre")
        else:
            nb_tours_accept="oui"
    
    for player in liste_joueurs:
        player["pieces"]=5
        
    plateau=[1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
    shuffle(plateau)
    etoile=randint(0,len(plateau))
    prix_etoile=10
    return [tours,plateau,etoile,prix_etoile]

def mini_jeux(liste_mini_jeux,pseudos_joueurs,liste_joueurs):
    """
    lance un mini jeu au hazard entre le puissance 4, le morpion et le plus gros score aux dés.
    :param liste_mini_jeux: (list)
    :param pseudos_joueurs: (list)
    :param liste_joueurs: (list) liste de dictionnaires
    :CU: les mini-jeux de a liste peuvent être lancés
    """
    print('\n'*4)
    print("Lancement d'un mini-jeu !")
    jeu=liste_mini_jeux[randint(0,len(liste_mini_jeux)-1)]
    if len(pseudos_joueurs)>2:
        j1=pseudos_joueurs[randint(0,len(pseudos_joueurs)-1)]
        j2=j1
        while j2==j1:
            j2=pseudos_joueurs[randint(0,len(pseudos_joueurs)-1)]
        print("Les joueurs tirés au sort sont : ",j1,'et',j2)
    else:
        j1=pseudos_joueurs[0]
        j2=pseudos_joueurs[1]
        print(j1,"et",j2,"vous allez donc vous affronter")
        
    
    if jeu=='p4':
        print("Le jeu choisi aléatoirement est : le puissance 4!")
        print()
        print(j1,'vous êtes le joueur n°1')
        print(j2,'vous êtes le joueur n°2')
        print()
        puissance4=p4()
        if puissance4==1:
            print(j1, 'vous avez battu',j2,'vous gagnez donc 1 étoile !')
            for p in liste_joueurs:
                if p["pseudo"]==j1:
                    p["nb_win_tot"]+=1
                    p["etoiles"]+=1
                    print("Vous en avez donc maintenant",p["etoiles"])
        if puissance4==2:
            print(j2, 'vous avez battu',j1,'vous gagnez donc 1 étoile !')
            for p in liste_joueurs:
                if p["pseudo"]==j2:
                    p["nb_win_tot"]+=1
                    p["etoiles"]+=1
                    print("Vous en avez donc maintenant",p["etoiles"])
        if puissance4==0:
            print(j1, ', ',j2,', vous avez fait match nul, chacun de vous gagne 10 pièces')
            for p in liste_joueurs:
                if p["pseudo"]==j1 or p["pseudo"]==j2:
                    p["pieces"]+=10
                    print(p["pseudo"],"vous en avez donc maintenant",p["pieces"])
                    
    elif jeu=='morpion':
        print("Le jeu choisi aléatoirement est : le morpion!")
        print()
        print(j1,'vous êtes le joueur n°1')
        print(j2,'vous êtes le joueur n°2')
        print()
        m=morpion()
        if m==1:
            print(j1, 'vous avez battu',j2,'vous gagnez donc 1 étoile !')
            for p in liste_joueurs:
                if p["pseudo"]==j1:
                    p["nb_win_tot"]+=1
                    p["etoiles"]+=1
                    print("Vous en avez donc maintenant",p["etoiles"])
        if m==2:
            print(j2, 'vous avez battu',j1,'vous gagnez donc 1 étoile !')
            for p in liste_joueurs:
                if p["pseudo"]==j2:
                    p["nb_win_tot"]+=1
                    p["etoiles"]+=1
                    print("Vous en avez donc maintenant",p["etoiles"])
        if m==0:
            print(j1, ', ',j2,', vous avez fait match nul, chacun de vous gagne 10 pièces')
            for p in liste_joueurs:
                if p["pseudo"]==j1 or p["pseudo"]==j2:
                    p["pieces"]+=10
                    print(p["pseudo"],"vous en avez donc maintenant",p["pieces"])
    
    elif jeu=='dés':
        print("Le jeu choisi aléatoirement est : la battaille de dés!")
        print()
        j_d=jeu_des(j1,j2)
        g=j_d[0]
        k=j_d[1]
        if g==j1:
            print(j1,"vous avez battu",j2,"en",k,"tours, vous gagnez donc",k,'fois 5 pieces')
            for p in liste_joueurs:
                if p["pseudo"]==j1:
                    p["pieces"]+=5*k
                    p["nb_win_tot"]+=1
                    print("Vous en avez donc maintenant",p["pieces"])
        if g==j2:
            print(j2,"vous avez battu",j1,"en",k,"tours, vous gagnez donc",k,'fois 5 pieces')
            for p in liste_joueurs:
                if p["pseudo"]==j2:
                    p["pieces"]+=5*k
                    p["nb_win_tot"]+=1
                    print("Vous en avez donc maintenant",p["pieces"])
    print()
            
def objets(liste_joueurs,j,pseudos_joueurs,nb_joueurs,liste_obj):
    """
    permet l'utilisation d'objets pour les joueurs s'ils en ont
    :param liste_joueurs: (list) liste de dictionnaires
    :param j: (int)
    :param pseudos_joueurs:(list)
    :param nb_joueurs: (int)
    :param liste_obj: (list)
    :CU: les dictionnaires de la liste liste_joueurs contiennent les clés "objets", "pseudo","pieces","etoiles","dé"
    """
    if len(liste_joueurs[j]["objets"])!=0:
        
        print(liste_joueurs[j]["pseudo"],"vous avez",liste_joueurs[j]["objets"],"comme objet(s)")
        
        use_obj_fait="non"
        while use_obj_fait!="oui":
            demande_obj=input("Utiliser un objet? :  ")
            try:
                assert demande_obj=="oui" or demande_obj=="non"
            except AssertionError:
                print("Répondre oui ou non")
            else:
                use_obj_fait="oui"
        

        if demande_obj=="oui":
            
            if len(liste_joueurs[j]["objets"])>1:
                
                choix_objet="non"
                while choix_objet!="oui":
                    choix_obj=input("Choisissez quel objet utiliser")
                    try:
                        assert choix_obj in liste_joueurs[j]["objets"]
                    except AssertionError:
                        print("Vous ne possédez pas l'objet")
                    else:
                        choix_objet="oui"
                    
            else:
                choix_obj=liste_joueurs[j]["objets"][0]
            
            
            if nb_joueurs==2:
                li=list(liste_joueurs)
                for p in li:
                    if p["pseudo"]==liste_joueurs[j]["pseudo"]:
                        li.remove(p)
                choix_adv=li[0]
                choix_fait="oui"
                
            if nb_joueurs>2:
                choix_fait="non"
            
            if nb_joueurs>1:
                
                if choix_obj=="vol 5pcs adv":
                    joueurs_possibles=list(pseudos_joueurs)
                    joueurs_possibles.remove(liste_joueurs[j]["pseudo"])
                    for p in liste_joueurs:
                        if p["pieces"]<5:
                            if p!=liste_joueurs[j]:
                                joueurs_possibles.remove(p["pseudo"])
                        if p["pseudo"]==liste_joueurs[j]["pseudo"]:
                            print("vous possedez",p["pieces"],"pieces")
                        else:
                            print(p["pseudo"], "possède", p["pieces"],'pieces')
                    
                    if len(joueurs_possibles)!=0:
                        if len(joueurs_possibles)==1:
                            choix_adv=joueurs_possibles[0]
                        
                        elif len(joueurs_possibles)>1:
                            while choix_fait!="oui":
                                choix_adv=input("Sur quel adversaire souhaitez-vous utiliser l'objet? :  ")
                                try:
                                    assert choix_adv in pseudos_joueurs and choix_adv!=liste_joueurs[j]["pseudo"]
                                except AssertionError:
                                    print("Le pseudo est mal orthographié ou vous voulez utiliser l'objet sur vous même, ce qui est impossible")
                                else:
                                    choix_fait="oui"
                                    
                       
                            
                        for p in liste_joueurs:
                            if p["pseudo"]==choix_adv:
                                p["pieces"]=p["pieces"]-5
                                liste_joueurs[j]["pieces"]+=5
                                print("Vous avez volé 5 pièces à",p["pseudo"])
                                print("Il en a désormais",p["pieces"],"et vous",liste_joueurs[j]["pieces"])
                    else:
                        print("Personne n'a assez de pièces! L'objet est inutilisable pour l'instant") 

                    
                    
                if choix_obj=="vol 1 etoile adv":
                    joueurs_possibles=list(pseudos_joueurs)
                    joueurs_possibles.remove(liste_joueurs[j]["pseudo"])
                    for p in liste_joueurs:
                        if p["etoiles"]==0:
                            if p!=liste_joueurs[j]:
                                joueurs_possibles.remove(p["pseudo"])
                        if p["pseudo"]==liste_joueurs[j]["pseudo"]:
                            print("Vous possedez",p["etoiles"],"etoile(s)")
                        else:
                            print(p["pseudo"], "possède", p["etoiles"],'etoile(s)')
                    
                    if len(joueurs_possibles)!=0:
                        if len(joueurs_possibles)==1:
                            choix_adv=joueurs_possibles[0]
                            
                        elif len(joueurs_possibles)>1:
                            while choix_fait!="oui":
                                choix_adv=input("Sur quel adversaire souhaitez-vous utiliser l'objet? :  ")
                                try:
                                    assert choix_adv in joueurs_possibles and choix_adv!=liste_joueurs[j]["pseudo"]
                                except AssertionError:
                                    print("Le pseudo est le votre, mal orthographié ou celui d'un joueur qui n'a pas d'étoiles")
                                else:
                                    choix_fait="oui"
                        
                        for p in liste_joueurs:
                            if p["pseudo"]==choix_adv:
                                p["etoiles"]=p["etoiles"]-1
                                liste_joueurs[j]["etoiles"]+=1
                                print("Vous avez volé une étoile à",p["pseudo"],'qui en a maintenant',p["etoiles"])
                                print("Vous avez maintenant",liste_joueurs[j]["etoiles"],'étoile(s)')
                    else:
                        print("Personne ne possède d'étoile! L'objet est inutilisable pour l'instant")
                
                
                if choix_obj=="-3 dé adv":
                    joueurs_possibles=list(pseudos_joueurs)
                    print("Les joueurs sont :",end=' ')
                    for p in joueurs_possibles:
                        print(p,end='  ')
                    while choix_fait!="oui":
                        choix_adv=input("Sur quel adversaire souhaitez-vous utiliser l'objet? :  ")
                        try:
                            assert choix_adv in joueurs_possibles and choix_adv!=liste_joueurs[j]["pseudo"]
                        except AssertionError:
                            print("Le pseudo est mal orthographié ou vous voulez utiliser l'objet sur vous même, ce qui est impossible")
                        else:
                            choix_fait="oui"
                    for p in liste_joueurs:
                        if p["pseudo"]==choix_adv:
                            p["dé"]=p["dé"]-3
                
                if choix_obj=="+3 son dé":
                    liste_joueurs[j]["dé"]+=3
                
                liste_joueurs[j]["objets"].remove(choix_obj)
                
            elif nb_joueurs==1:
                if choix_obj=="+3 son dé":
                    liste_joueurs[j]["dé"]+=3
                    liste_joueurs[j]["objets"].remove(choix_obj)
                else:
                    print("L'objet n'est pas utilisable en jouant seul")
            print()
            
def avancer(liste_joueurs,plateau,etoile,prix_etoile,j,liste_obj):
    """
    déplace le joueur et lui ajoute, enlève des pièces, objets, étoiles selon les cases sur lesquelles le joueur passe
    retourne la nouvelle place le l'etoile (peut rester la même)
    :param liste_joueurs: (list)
    :param plateau: (list)
    :param etoile: (int)
    :param prix_etoile: (int)
    :param j: (int)
    :param liste_obj: (list)
    :CU: liste_joueurs contient des dictionnaires qui contiennent les clés "objets", "pseudo","pieces","etoiles","dé"
    """
    print(liste_joueurs[j]["pseudo"],end=" ")
    print("Vous avez un dé à",liste_joueurs[j]["dé"],"faces")
    lancé=input("appuyez sur entrée pour lancer le dé  ")
    dé=randint(1,liste_joueurs[j]["dé"])
    print("Vous avez fait :  ",dé)
    
    bouge_etoile=False
    k=0
    while k<dé:
        liste_joueurs[j]["position"]+=1
        liste_joueurs[j]["position"]=liste_joueurs[j]["position"]%len(plateau)
        bouge_perso(liste_joueurs,plateau)
        k+=1
        if k==dé:
            CASE=plateau[liste_joueurs[j]["position"]]
            if CASE==1:
                liste_joueurs[j]["pieces"]+=3
                print("Case verte : vous gagnez 3 pièces, vous en avez desormais",liste_joueurs[j]["pieces"])
            if CASE==2:
                if liste_joueurs[j]["pieces"]>2:
                    liste_joueurs[j]["pieces"]=liste_joueurs[j]["pieces"]-3
                    print("Case rouge : vous perdez 3 pièces, vous en avez desormais",liste_joueurs[j]["pieces"])
            if CASE==3:
                objet_gagné=[liste_obj[randint(0,len(liste_obj)-1)]]
                liste_joueurs[j]["objets"]+=objet_gagné
                liste_joueurs[j]["nb_obj_tot"]+=1
                print("Case bleue : vous gagnez un objet aleatoire : ",objet_gagné)

        if liste_joueurs[j]["position"]==etoile:
            if liste_joueurs[j]["pieces"]>=prix_etoile:
                print("Vous avez",liste_joueurs[j]["pieces"],"pieces, vous pouvez acheter l'étoile pour 5 pieces")
                achat=""
                while achat!="oui" and achat!="non":
                    achat=input("Acheter l'etoile? :  ")
                    try:
                        assert achat=="oui" or achat=="non"
                    except AssertionError:
                        print("Répondre oui ou non")
                if achat=="oui":
                    bouge_etoile=True
                    liste_joueurs[j]["etoiles"]+=1
                    liste_joueurs[j]["pieces"]=liste_joueurs[j]["pieces"]-5
                    print("Vous avez maintenant",liste_joueurs[j]["etoiles"],'étoile(s) et',liste_joueurs[j]["pieces"],'pièce(s)')
            else:
                print("L'étoile coûte",prix_etoile,'pieces, vous n\'en avez que',liste_joueurs[j]["pieces"])
        
        
    if bouge_etoile == True :
        nv_etoile=randint(0,len(plateau))
        etoile=nv_etoile
        place_etoile(etoile,plateau)
        
    liste_joueurs[j]["nb_cases_tot"]+=dé
        
    return etoile

def etoiles_bonus(liste_joueurs):
    '''
    ajoute une étoile aux joueurs ayant parcouru le plus de cases, ayant le plus d'objets et ayant gagné le plus de mini-jeux
    :param liste_joueurs: (list)
    :CU: liste_joueurs contient des dictionnaires qui contiennent les clés "objets", "pseudo","pieces","etoiles","dé"
    '''
    liste_gagnant_obj=[]
    for joueur in liste_joueurs:
        liste_gagnant_obj.append([joueur["nb_obj_tot"],joueur["pseudo"]])
    liste_gagnant_obj.sort(reverse=True)
    if liste_gagnant_obj[0][0]!=0:
        if liste_gagnant_obj[0][0]!=liste_gagnant_obj[1][0]:
            print(liste_gagnant_obj[0][1],"est le joueur ayant gagné le plus de d'objets (",liste_gagnant_obj[0][0],"), il gagne une étoile bonus")
            gagnant_obj=liste_gagnant_obj[0][1]
        else:
            print("2 joueurs ou plus sont ex aequo en nombre d'objets gagnés, aucun ne gagne d'étoile bonus")
            gagnant_obj="!"
    else:
        gagnant_obj="!"
    
    liste_gagnant_cases=[]
    for joueur in liste_joueurs:
        liste_gagnant_cases.append([joueur["nb_cases_tot"],joueur["pseudo"]])
    liste_gagnant_cases.sort(reverse=True)
    if liste_gagnant_cases[0][0]!=0:
        if liste_gagnant_cases[0][0]!=liste_gagnant_cases[1][0]:
            print(liste_gagnant_cases[0][1],"est le joueur ayant parcouru le plus de cases (",liste_gagnant_cases[0][0],"), il gagne une étoile bonus")
            gagnant_cases=liste_gagnant_cases[0][1]
        else:
            print("2 joueurs ou plus sont ex aequo en nombre de cases parcourures, aucun ne gagne d'étoile bonus")
            gagnant_cases="!"
    else:
        gagnant_cases="!"
        
    liste_gagnant_win=[]
    for joueur in liste_joueurs:
        liste_gagnant_win.append([joueur["nb_win_tot"],joueur["pseudo"]])
    liste_gagnant_win.sort(reverse=True)
    if liste_gagnant_win[0][0]!=0:
        if liste_gagnant_win[0][0]!=liste_gagnant_win[1][0]:
            print(liste_gagnant_win[0][1],"est le joueur ayant gagné le plus de mini-jeux (",liste_gagnant_win[0][0],"), il gagne une étoile bonus")
            gagnant_win=liste_gagnant_win[0][1]
        else:
            print("2 joueurs ou plus sont ex aequo en nombre de mini-jeux gagnés, aucun ne gagne d'étoile bonus")
            gagnant_win="!"
    else:
        gagnant_win="!"
            
    for j in liste_joueurs:
        if j["pseudo"]==gagnant_win or j["pseudo"]==gagnant_cases or j["pseudo"]==gagnant_obj:
            j['etoiles']+=1


def gagnant(liste_joueurs,nb_joueurs):
    '''
    retourne le gagnant de la partie soit celui qui a le plus d'etoiles, si ex-aequo le nombre de pieces puis classés par nom si ex-aequo
    :param liste_joueurs: (list)
    :param nb_joueurs: (int)
    :CU: liste_joueurs contient des dictionnaires qui contiennent les clés "pseudo","pieces","etoiles"
    '''
    liste_gagnant=[]
    for joueur in liste_joueurs:
        liste_gagnant.append([joueur["etoiles"],joueur["pieces"],joueur["pseudo"]])
    liste_gagnant.sort(reverse=True)
    for i in range(nb_joueurs):
        if i==0:
            print(i+1,"er :", liste_gagnant[i][2],"avec", liste_gagnant[i][0],"etoile(s) et", liste_gagnant[i][1],"pieces")
        elif i==1:
            print(i+1,"nd :", liste_gagnant[i][2],"avec", liste_gagnant[i][0],"etoile(s) et", liste_gagnant[i][1],"pieces")
        else:
            print(i+1,"eme :", liste_gagnant[i][2],"avec", liste_gagnant[i][0],"etoile()s et", liste_gagnant[i][1],"pieces")
    return liste_gagnant[0][2]
        

def fichier(liste_joueurs,tours,gagne):
    """
    écrit dans le fichier textre 'fichier_scores.txt' le résultat et classement de la partie
    :param liste_joueurs: (list)
    :param tours: (int)
    :param gagne: (str)
    :CU: liste_joueurs contient des dictionnaires qui contiennent les clés "pseudo","pieces","etoiles","nb_obj_tot","nb_cases_tot","nb_win_tot"
    """
    with open('fichier_scores.txt','at',encoding='utf-8') as fichier:
        for p in liste_joueurs:
            t=('  ',p["pseudo"]," : ", p["etoiles"]," étoiles, ",p["pieces"]," pièces, ",p["nb_obj_tot"]," objet(s) au total, ",p["nb_cases_tot"]," case(s) parcourue(s), ",p["nb_win_tot"]," victoire(s) aux mini-jeux, ")
            for s in t:
                fichier.write(str(s))
            fichier.write('\n')
            fichier.write(tours)
            fichier.write(' tours joués \n')
        fichier.write(gagne)
        fichier.write('est le gagnant')
        fichier.write('\n \n')



def clear_shell():
    '''
    affiche 20 lignes vides
    '''
    print('\n' * 20)

if __name__=="__main__":
    jeu()
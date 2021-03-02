package strategy;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import cTypes.League;
import competition.Competitor;
import competition.Strategy;
import exception.InvalidNbOfCompetitorsException;

public class Poules3Meilleurs2Et2MTroisiemes extends Strategy {

	public Poules3Meilleurs2Et2MTroisiemes() {
		super();
	}

	@Override
	public List<Competitor> selectCompetitors(List<League> poules) {
		// utilisation d'un compteur pour prendre les 2 premiers et d'une liste pour avoir les 2 meilleurs 3èmes
		
		// resultat final
		List<Competitor> res = new ArrayList<Competitor>();
		
		// tampon pour garder les meilleurs 3emes
		List<Competitor> meilleursTroisiemes = new ArrayList<Competitor>();
		
		
		for(League poule : poules) {
			int competiteurNum = 0;
			Map<Competitor,Integer> ranked = poule.ranking();
			for (Map.Entry<Competitor,Integer> c : ranked.entrySet()) {
				
				// si le competiteur est un des deux meilleurs on l'ajoute au resultat
				if (competiteurNum<2) {
					res.add(c.getKey());
				}
				
				// si il est 3 eme on verifie qu'il soit l'un des meilleurs pour l'ajouter plus tard ou non sinon 
				if (competiteurNum == 2) {
					
					// je prefere imbriquer les if ici prcq je ne suis pas certain qu'il ne vérifie que le 1er et je veux eviter des pbs d'indice
					if (meilleursTroisiemes.size()<2) {  

						 meilleursTroisiemes.add(c.getKey());
					}
					
					// surement moyen de mieux faire pour les else et l'utilisation des listes
					else if  (c.getValue() > meilleursTroisiemes.get(1).getPoints()) {


						
						meilleursTroisiemes.remove(1);
						meilleursTroisiemes.add(c.getKey());
					}
					else if (c.getValue() > meilleursTroisiemes.get(0).getPoints()) {
						meilleursTroisiemes.add(0,c.getKey());   //surtout ici où je crée complètement une autre liste je pense
						meilleursTroisiemes.remove(1);  
					}
					
					
				}

				competiteurNum++;
				
			}
		}
		
		// ajout des 2 meilleurs 3emes : 
		for (Competitor c : meilleursTroisiemes) res.add(c);
		return res;
	}

	
	
	@Override
	public List<League> createGroupStage(List<Competitor> comp) throws InvalidNbOfCompetitorsException {
		// idem : possible de faire donc une classe abstraite avec la définition de cette fonction avec un param entier
		// 	qui permet de créer le nombre de poules qu'on veut
		// 	TODO si j'en ai le temps.
				
		
		// Au moins 8 Competitor sinon impossible de jouer le tournois :
		//	Tous les Competiteurs seront pris si il y en a 8, les 2 premiers à chaque fois donc 6 + les 2 meilleurs 3èmes (il n'y en 
		//	a que 2, donc tous) qui fera 8 competiteurs : ils seront tous pris		
		if (comp.size()<8) throw new InvalidNbOfCompetitorsException();
		
		List<List<Competitor>> leaguesComps = new ArrayList<List<Competitor>>();
		leaguesComps.add(new ArrayList<Competitor>());
		leaguesComps.add(new ArrayList<Competitor>());
		leaguesComps.add(new ArrayList<Competitor>());
		List<League> res = new ArrayList<League>();
		
		int i = 0;
		for (Competitor c : comp) {
			leaguesComps.get(i).add(c);
			i = (i+1)%3;
		}
		
		res.add(new League(leaguesComps.get(0)));
		res.add(new League(leaguesComps.get(1)));
		res.add(new League(leaguesComps.get(2)));
		return res;
	}

}


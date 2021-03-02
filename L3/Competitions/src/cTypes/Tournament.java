package cTypes;

import java.util.ArrayList;
import java.util.List;

import exception.InvalidNbOfCompetitorsException;
import competition.Competition;
import competition.Competitor;

public class Tournament extends Competition {

	public Tournament(List<Competitor> competitors) {
		super(competitors);
	}
	
	
	/**
	 * renvoie le nb de points maximum obtenu par un competiteur jusqu'à lors
	 * @return int nb points
	 */
	public int maxPoints() {
		int res = 0;
		for (Competitor c : this.getCompetitors()) {
			int pts = c.getPoints();
			if (pts>res) res=pts;
		}
		return res;
	}
	
	
	
	
	@Override
	public void play(List<Competitor> competitors) throws InvalidNbOfCompetitorsException {
		List<List<Competitor>> matchs = this.organizeMatchs();
		int tour = 1;
		while (matchs.size()!=0) {     // tant que des matchs sont encore faisables (au moins 2 competiteurs avec le meme nb de pts)
										// sinon on a un vainqueur 
			System.out.println();
			System.out.println("Tour n°"+tour);
			for (List<Competitor> match : matchs) {
				this.playMatch(match.get(0), match.get(1));
			}
			matchs = this.organizeMatchs();  // tour suivant
			tour++;
		}
	}
	
	/**
	 * renvoie true si n  est une puissance de 2
	 * @param n l'entier à verifier
	 * @return boolean true si n est une puissance de 2, false sinon
	 */
	private static boolean isApowerOfTwo(int n) {
		
		if (n%2 == 0) return isApowerOfTwo(n/2);
		else return n==1;
	}
	
	
	@Override
	// je crée les tours du tournois par rapport au nb de pts, si nb de pts égaux et maximal : même tour à jouer
	// si moins de pts qu'un autre -> éliminé
	// si un seul joueur ayant le nb de pts max, il a gagné
	public List<List<Competitor>> organizeMatchs() throws InvalidNbOfCompetitorsException {
		if (!isApowerOfTwo(this.getCompetitors().size())) throw new InvalidNbOfCompetitorsException("Le nb de competiteurs n'est pas une puissance de 2 donc on ne peut pas faire un tournois");
		int maxPts = this.maxPoints();
		int indexRes = 0;
		int i = 0;
		int j = 1;
		List<List<Competitor>> res = new ArrayList<List<Competitor>>();
		while (i<this.getCompetitors().size() && j<this.getCompetitors().size()) {
			Competitor c1 = this.getCompetitors().get(i);
			Competitor c2 = this.getCompetitors().get(j);
			if (c1.getPoints() < maxPts) {
				i++;
				j++;
			}
			else if (c1.getPoints() == c2.getPoints() ) {
				List<Competitor> match = new ArrayList<Competitor>();
				match.add(0,c1);
				match.add(1,c2);
				res.add(indexRes,match);
				i=j+1;
				j=i+1;
				
			}
			else j++;
		}
		return res;
		
	}


}

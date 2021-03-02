package mTypes;

import competition.Competitor;
import competition.Match;

public class MatchAlea implements Match {

	
	/**
	 * renvoie le gagnant d'un match aleatoire  //devrait être static?
	 * @param c1 Competitor 1er competiteur
	 * @param c2 Competitor 2eme competiteur
	 * @return Competitor le competiteur gagnant 
	 */
	public  Competitor getWinner(Competitor c1,Competitor c2){
		if (Math.random()>=0.5) return c1;
		return c2;
	}

}

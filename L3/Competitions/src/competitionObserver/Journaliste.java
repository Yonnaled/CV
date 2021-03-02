package competitionObserver;

import competition.Competitor;

public class Journaliste implements CompetitionObserver{
	/**
	 * Observer Journaliste qui affiche les resultats de chaque match
	 */
	
	@Override
	public void react(Competitor c1, Competitor c2)  {
		System.out.println(c1 + " vs "+ c2 + " --> " + c1 + " wins!");
	}

}

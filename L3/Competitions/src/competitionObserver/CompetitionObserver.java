package competitionObserver;

import competition.Competitor;

public interface CompetitionObserver {
	
	/**
	 * react with c1 winner and c2 loser
	 * @param c1 Competitor winner
	 * @param c2 Competitor loser
	 */
	public void react(Competitor c1, Competitor c2);
}
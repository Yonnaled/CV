package competition;

public interface Match {
	/**
	 * renvoie le gagnant du match entre le competiteur 1 et le competiteur 2 selon la definition du match
	 * @param c1 competiteur 1
	 * @param c2 competiteur 2
	 * @return Competitor le gagnant du match
	 */
	public  Competitor getWinner(Competitor c1, Competitor c2);
}

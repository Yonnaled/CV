package competition;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import competitionObserver.CompetitionObserver;
import exception.InvalidNbOfCompetitorsException;
import util.MapUtil;	
import mTypes.MatchAlea;



public abstract class Competition {
	private final Match match;
	private final List<Competitor> competitors;
	protected List<CompetitionObserver> observers; 

	public Competition(List<Competitor> myCompetitors) {
		this.competitors = myCompetitors;
		this.match = new MatchAlea();
		this.observers = new ArrayList<CompetitionObserver>();
	}
	
	/** competitors Getter
	 * @return which is competitors attribute
	**/
	public List<Competitor> getCompetitors(){
		return this.competitors;
	}


	/**
	 * ajoute l'observer à la liste (attribut observers de l'objet) 
	 * @param co CompetitionObserver  l'observer à ajouter à la liste
	 */
	public void addCompetitionObserver(CompetitionObserver co) {
		this.observers.add(co);
	}
	
	/**
	 * supprime l'observer de la liste (attribut observers de l'objet) s'il existe, sinon rien ne se passe
	 * @param co CompetitionObserver  l'observer à retirer de la liste
	 */
	public void deleteCompetitionObserver(CompetitionObserver co) {
		this.observers.remove(co);
	}
	
	/**
	 * Notify competitions observers
	 * @param c1 competiteur 1
	 * @param c2 competiteur 2
	 */
	public void notifyObservers(Competitor c1, Competitor c2) {
		for (CompetitionObserver co : this.observers) {
			co.react(c1, c2);
		}
	}

	/**
	 * organise les matchs, les fait jouer, ajoute les pts et fait le ranking
	 * (fait appel à la méthode abstraite du meme nom mais avec une liste de competiteurs)
	 */
	public void play(){
		try {
			play(this.getCompetitors());
			this.affiche();
		}
		catch (Exception e) {
			System.out.println(e);
		}
	}

	
	
	/**
	 *
	 * @param competitors liste de competiteurs
	 * @throws InvalidNbOfCompetitorsException si nombre de competiteurs invalide
	 */
	protected abstract void play(List<Competitor> competitors) throws InvalidNbOfCompetitorsException;

	
	
	/**
	 *  Fait jouer un match entre c1 et c2, ajoute le point au gagnant et renvoie le gagnant
	 * @param c1 Competitor le 1er competiteur de ce match
	 * @param c2 Competitor le 2nd competiteur de ce match
	 * @return Competitor le gagnant du match
	 */
	public Competitor playMatch(Competitor c1, Competitor c2){
		Competitor res = this.match.getWinner(c1,c2);
		if (c1 == res) this.notifyObservers(res, c2);
		else this.notifyObservers(c1, res);
		res.addPoints();
		return res;
	}

	
	
	
	/**
	 * organise les matchs selon le type de competition :  méthode abstraite
	 * @throws InvalidNbOfCompetitorsException si nombre de competiteurs invalide
	 * @return  la liste des matchs qui vont être joués
	 */
	public abstract List<List<Competitor>> organizeMatchs() throws InvalidNbOfCompetitorsException;
	
	
	
	
	/**
	 * fait le classement des competiteurs à l'issue de la competition
	 * @return map competitor , int 
	 */
	public Map<Competitor,Integer> ranking(){
		Map<Competitor,Integer> notRanked = new HashMap<Competitor,Integer>();
		for (Competitor c : this.getCompetitors()) {
			notRanked.put(c, c.getPoints());
		}
		return MapUtil.sortByDescendingValue(notRanked);
	}
	
	/**
	 * affiche les resultats
	 */
	public void affiche() {
		Map<Competitor,Integer> ranked = this.ranking();
		System.out.println();
		System.out.println("*** Ranking ***");
		for (Map.Entry<Competitor, Integer> c : ranked.entrySet()) {
			System.out.println(c.getKey() + " - " + c.getValue());
		}
	}
}

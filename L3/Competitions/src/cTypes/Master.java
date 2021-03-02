package cTypes;


import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import competition.Strategy;
import competitionObserver.CompetitionObserver;
import competition.Competition;
import competition.Competitor;
import exception.InvalidNbOfCompetitorsException;




public class Master extends Competition {
	// J'ai choisi d'enregistrer les listes de poules (League) et  le tournois (Tournament) pour faciliter le ranking
	// tournament est défini dans play, en attendant il vaut null
	// poules est initialisé dans le constructeur si la Strategy peut créer des Leagues pour le nb de Competitor 
	// 	ex : 4 Competitors et 6 Leagues impossible
	
	private List<League> poules = null;
	private Tournament tournament = null;
	private final Strategy strategy;
	private List<Map<Competitor, Integer>> rankings = new ArrayList<Map<Competitor,Integer>>();

	public Master(List<Competitor> myCompetitors, Strategy s) {
		super(myCompetitors);
		this.strategy = s;
		try {
			this.poules = this.strategy.createGroupStage(myCompetitors);
		}catch(InvalidNbOfCompetitorsException e) {
			System.out.println("Le nombre de competiteurs de correspond pas à l'utilisation de la stratégie utilisée");
		}
	}

	/**
	 * Joue la phase de poules grâce à this.poules
	 * appelle la stratégie de selection pour choisir les constructeurs qui vont au tournois
	 * joue le tournois
	 * @param competitors la liste les competiteurs qui vont jouer le Master
	 */
	public void play(List<Competitor> competitors) throws InvalidNbOfCompetitorsException {

		for (League p : this.poules) {
			for (CompetitionObserver o : this.observers) {
				p.addCompetitionObserver(o);
			}
		}
		this.playGroupStage();
		this.rankForLeague();
		List<Competitor> selectedCompetitors = this.strategy.selectCompetitors(this.getPoules());
		this.setTournament(selectedCompetitors);
		for (CompetitionObserver o : observers) {
			this.tournament.addCompetitionObserver(o);
		}
		for (Competitor c : selectedCompetitors) {
			// remet les pts à 0 pour jouer le tournois, surement pas la meilleure solution prcs qui faut 
			// faire enregistrer le ranking actuel via une autre methode que ranking 
			c.toZero();
		}
		this.tournament.play(selectedCompetitors);
		this.rankForTournament();

	}

	

	/**
	 * joue la phase de poules
	 */
	private void playGroupStage() {
		for (League poule : this.getPoules()) {
				try {
					poule.play(poule.getCompetitors());
				} catch (InvalidNbOfCompetitorsException e) {
					e.printStackTrace();
				}
			
		}
	}


	/**
	 * fait le classement pour les poules
	 */
	private void rankForLeague() {
		// avant que je ne remette à 0 les points pour jouer le tournois, cf methode play
		for (League poule : this.getPoules()) {
			this.addToRankings(poule.ranking());
		}
		
	}
	
	/**
	 * Fait le classement pour le tournois
	 */
	private void rankForTournament() {
		// fait le classement pour le ranking
		this.addToRankings(this.getTournament().ranking());
	}
	
	@Override
	public void affiche() {
		// pas besoin de faire le ranking ici, celui vraiment utile est fait dans le play
		// le ranking() existe toujours mais donne le nb de match gagnés en tout ce qui n'a pas vrmt de sens comme dit dans le sujet
		System.out.println();
		System.out.println("*** Ranking ***");
		
		List<Map<Competitor, Integer>> liste = this.getRankings();

		//pour chaque ranking dans la liste des rankings (ceux des Leagues et du tournois)
		int i = 0;
		for (Map<Competitor, Integer> ranking : liste) {  
			System.out.println();
			if (i<liste.size()-1) {
				System.out.println("Poule n°"+ Integer.toString(i+1));
			
				//Pour chaque <Competitor,Integer>
				for (Map.Entry<Competitor, Integer> c : ranking.entrySet()) {	
					System.out.println(c.getKey() + " - " + c.getValue().intValue());
				}
			}
			else {
				System.out.println("Résultats du tournois");
				int j=1;
				for (Map.Entry<Competitor, Integer> c : ranking.entrySet()) {
					String det = "er(e)  =>  Grand(e) Vainqueur(e)";
					if (j!=1) det = "ème"; 
					System.out.println(c.getKey() + " - " + j+det);
					j++;
				}
			}
			
			i++;
		}
	}

	@Override
	public List<List<Competitor>> organizeMatchs() throws InvalidNbOfCompetitorsException {
		return null;
	}
	
	

	/**
	 * @return the poules
	 */
	public List<League> getPoules() {
		return poules;
	}

	/**
	 * @return the strategy
	 */
	public Strategy getStrategy() {
		return strategy;
	}

	/**
	 * ajoute à la liste du classement
	 * @param ranking add ranking to rankings
	 */
	public void addToRankings(Map<Competitor, Integer> ranking) {
		rankings.add(ranking);
	}

	/**
	 * @return the tournament
	 */
	public Tournament getTournament() {
		return tournament;
	}


	/**
	 * @return the rankings
	 */
	public List<Map<Competitor,Integer>> getRankings(){
		return this.rankings;
	}
	
	/**
	 * setter pour tournament
	 */
	private void setTournament(List<Competitor> selectedCompetitors) {
		this.tournament = new Tournament(selectedCompetitors);
		
	}

}

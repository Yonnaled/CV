package competition;

import java.util.ArrayList;
import java.util.List;

import cTypes.*;
import competitionObserver.Bookmaker;
import competitionObserver.Journaliste;
import strategy.*;	

public class CompetitionMain {

	public static void main(String[] args) {
		List<Competitor> competitors = createCompetitors();
		
//		----------------------------------------------------
//		League myLeague = new cTypes.League(competitors);
//		myLeague.play();
//		----------------------------------------------------
//		Tournament myTournament = new cTypes.Tournament(competitors);
//		myTournament.play();
//		----------------------------------------------------
		
		Master myMaster = new cTypes.Master(competitors, new strategy4Poules.Poules4Meilleur1());
//		Master myMaster = new cTypes.Master(competitors, new strategy.Poules3Meilleurs2Et2MTroisiemes());
//		Master myMaster = new cTypes.Master(competitors, new strategy4Poules.LoserBracket4Poules());
		myMaster.addCompetitionObserver(new Journaliste());
		myMaster.addCompetitionObserver(new Bookmaker(competitors));
		
		System.out.println("Les poules sont :");
		for (League l : myMaster.getPoules()) {
			System.out.println(l.getCompetitors());
		}
		System.out.println();
		myMaster.play();
//		----------------------------------------------------

	}
	
	/**
	 * crée la liste des competiteurs pour le main
	 * @return la liste des competiteurs 
	 */
	public static List<Competitor> createCompetitors(){
		List<Competitor> res = new ArrayList<Competitor>();
		res.add(new Competitor("Vivian"));
		res.add(new Competitor("Milena"));
		res.add(new Competitor("Paul"));
		res.add(new Competitor("Geano"));
		res.add(new Competitor("Flopi"));
		res.add(new Competitor("Lukas"));
		res.add(new Competitor("Marion"));
		res.add(new Competitor("John"));
		
		res.add(new Competitor("Gladys"));
		res.add(new Competitor("Ines"));
		res.add(new Competitor("Hugo"));
		res.add(new Competitor("Kenzo"));
		res.add(new Competitor("Carololo"));
		res.add(new Competitor("Jean"));
		res.add(new Competitor("Toto"));
		res.add(new Competitor("Ali"));
		return res;
	}
	

}

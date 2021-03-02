package competitionTest;



import java.util.ArrayList;

import org.junit.Before;
import org.junit.Test;

import competition.Competitor;
import competition.Strategy;
import exception.InvalidNbOfCompetitorsException;

public abstract class StrategyTest {
	protected Strategy myStrat;
	private ArrayList<Competitor> myCompetitors;
	
	@Before
	public void init() {
		this.myCompetitors = new ArrayList<Competitor>();
		this.myCompetitors.add(new Competitor("Vivian"));
		this.myCompetitors.add(new Competitor("Milena"));
		this.myCompetitors.add(new Competitor("Polo"));
		this.myCompetitors.add(new Competitor("Geano"));
		this.myStrat = create();
	}
	
	protected abstract Strategy create();
	

	
	@Test
	public void createGroupStageTest() throws InvalidNbOfCompetitorsException{
		// cree des poules avec un nombre normal de competieus, n'est pas sensé lancer d'erreur
		this.myStrat.createGroupStage(this.myCompetitors);
	}
	
	@Test(expected=InvalidNbOfCompetitorsException.class)
	public void createGroupStageTestException() throws InvalidNbOfCompetitorsException {
		// init, je retire un competiteur de la liste pour en avoir un nombre invalide et lancer l'exception
		this.myCompetitors.remove(0);
		
		// je cree les poules avec un nombre invalide de competiteurs
		this.myStrat.createGroupStage(this.myCompetitors);
		
	}

}

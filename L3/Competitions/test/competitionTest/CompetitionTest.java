package competitionTest;

import java.util.ArrayList;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

import competition.Competition;
import competition.Competitor;

import static org.junit.Assert.*;

public abstract class CompetitionTest {
	protected Competition myCompetition;
	protected List<Competitor> myCompetitors;


	@Before
	public void init(){
		this.myCompetitors = new ArrayList<Competitor>();
		this.myCompetitors.add(new Competitor("Vivian"));
		this.myCompetitors.add(new Competitor("Milena"));
		this.myCompetition = this.createCompet();
	}

	
	protected abstract Competition createCompet();
	
	
	@Test
	public void testPlayMatch() {
		//init competiteurs
		Competitor vivian = this.myCompetitors.get(0);
		int nbPtsViv = vivian.getPoints();
		Competitor mil = this.myCompetitors.get(1);
		int nbPtsMil = mil.getPoints();
		
		//calcule le gagnant
		Competitor winner = this.myCompetition.playMatch(this.myCompetitors.get(0),this.myCompetitors.get(1));
		
		//verif points augmentent
		if (winner == mil) { 
			assertTrue(mil.getPoints()==nbPtsMil+1);
		}else assertTrue(vivian.getPoints()==nbPtsViv+1);
	}

}

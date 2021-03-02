package competitionTest;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import competition.Competitor;

public class CompetitorTest {
	private Competitor c; 
	
	
	@Before
	public void init() {
		this.c = new Competitor("Vivian");
		
	}

	@Test
	public void addPointsTest() {
		//init c : nb points de competiteur
		int points = this.c.getPoints();
		
		// ajout point
		c.addPoints();
		
		// verif point bien ajouté
		assertEquals(c.getPoints(),points+1);
	}
	
	@Test
	public void getNameTest() {
		assertSame(this.c.getName(),"Vivian");	 
	}
	
	@Test
	public void getPointsTest() {
		// init 
		int pts = this.c.getPoints();
		this.c.addPoints();
		
		// verif getPoints renvoie bien le nb de points
		assertTrue(this.c.getPoints()==pts+1);
	}
	

}

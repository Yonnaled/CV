package cTypesTest;


import java.util.List;

import org.junit.Test;

import cTypes.Tournament;
import exception.InvalidNbOfCompetitorsException;

import competition.Competition;
import competitionTest.CompetitionTest;
import competition.Competitor;

public class TournamentTest extends CompetitionTest {

	public Competition createCompet(){
		return new Tournament(this.myCompetitors);
	}
	
	

	@Test
	public void testOrganizeMatchsNeLancePasInvalidNbOfCompetitorsException() throws InvalidNbOfCompetitorsException {
		this.myCompetition.organizeMatchs();
	}

	
	@Test(expected= InvalidNbOfCompetitorsException.class)
	public void testOrganizeMatchsException() throws InvalidNbOfCompetitorsException {
		// init avec un nombre de competiteurs invalide
		List<Competitor> comp = this.myCompetitors;
		comp.add(new Competitor("TOTO BRUNET"));
		Tournament t = new Tournament(comp);
		
		// tentative d'organiser les matchs : doit renvoyer une exception
		t.organizeMatchs();
		
	}
}

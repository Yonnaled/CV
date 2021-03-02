package cTypesTest;


import cTypes.League;
import competition.Competition;
import competitionTest.CompetitionTest;

public class LeagueTest extends CompetitionTest {

	
	@Override
	protected Competition createCompet() {
		return new League(this.myCompetitors);
	}

	
}
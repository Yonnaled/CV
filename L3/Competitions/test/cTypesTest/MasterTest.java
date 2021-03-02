package cTypesTest;

import cTypes.Master;
import competition.Competition;
import competitionTest.CompetitionTest;

public class MasterTest extends CompetitionTest{
	

	@Override
	protected Competition createCompet() {
		return new Master(this.myCompetitors,new strategy4Poules.LoserBracket4Poules());
	}




}

package cTypes;

import java.util.ArrayList;
import java.util.List;

import competition.Competition;
import competition.Competitor;
import exception.InvalidNbOfCompetitorsException;

public class League extends Competition {

	public League(List<Competitor> competitors) {
		super(competitors);
	}

	@Override
	public void play(List<Competitor> competitors) throws InvalidNbOfCompetitorsException {

		// organizeMatchs
		List<List<Competitor>> matchs = this.organizeMatchs();
		// playMatchs
		for (List<Competitor> match : matchs) {
			this.playMatch(match.get(0), match.get(1));
		}
		
	}


	@Override
	public List<List<Competitor>> organizeMatchs(){
		List<List<Competitor>> res = new ArrayList<List<Competitor>>();
		int i = 0;
		for ( Competitor c1 : this.getCompetitors()) {
			for ( Competitor c2 : this.getCompetitors()) {
				List<Competitor> match = new ArrayList<Competitor>();
				if (c1 != c2) {
					match.add(0,c1);
					match.add(1,c2);
					res.add(i,match);
					i++;
				}
				
			}
		}	
	
		return res;
	}
	

}

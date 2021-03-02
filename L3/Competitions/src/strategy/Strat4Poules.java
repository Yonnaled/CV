package strategy;

import java.util.ArrayList;
import java.util.List;

import cTypes.League;
import competition.Competitor;
import competition.Strategy;
import exception.InvalidNbOfCompetitorsException;

public abstract class Strat4Poules extends Strategy {

	public Strat4Poules() {
		super();
	}

	@Override
	public abstract List<Competitor> selectCompetitors(List<League> poules);

	
	@Override
	public List<League> createGroupStage(List<Competitor> comp) throws InvalidNbOfCompetitorsException {	
		// possible de faire d'autres tests dans les sous classes si je veux qu'il y ait plus de joueurs minimum
		if (comp.size()<4) throw new InvalidNbOfCompetitorsException();
		
		List<List<Competitor>> leaguesComps = new ArrayList<List<Competitor>>();
		leaguesComps.add(new ArrayList<Competitor>());
		leaguesComps.add(new ArrayList<Competitor>());
		leaguesComps.add(new ArrayList<Competitor>());
		leaguesComps.add(new ArrayList<Competitor>());
		List<League> res = new ArrayList<League>();
		
		int i = 0;
		for (Competitor c : comp) {
			leaguesComps.get(i).add(c);
			i = (i+1)%4;
		}
		
		res.add(new League(leaguesComps.get(0)));
		res.add(new League(leaguesComps.get(1)));
		res.add(new League(leaguesComps.get(2)));
		res.add(new League(leaguesComps.get(3)));
		return res;

	}


}

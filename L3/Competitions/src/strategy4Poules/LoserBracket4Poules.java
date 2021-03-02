package strategy4Poules;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import cTypes.League;
import competition.Competitor;
import strategy.Strat4Poules;

public class LoserBracket4Poules extends Strat4Poules {

	public LoserBracket4Poules() {
		super();
	}

	@Override
	public List<Competitor> selectCompetitors(List<League> poules) {

		List<Competitor> res = new ArrayList<Competitor>();
		for(League poule : poules) {
			int i = 0;
			int nbComp = poule.getCompetitors().size();
			Map<Competitor,Integer> ranked = poule.ranking();
			for (Map.Entry<Competitor,Integer> c : ranked.entrySet()) {
				if (i == nbComp-1) res.add(c.getKey());
				i++;
			}
		}
		return res;
	}

	
	
	

}

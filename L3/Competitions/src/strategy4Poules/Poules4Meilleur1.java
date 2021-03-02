package strategy4Poules;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import cTypes.League;
import competition.Competitor;
import strategy.Strat4Poules;

public class Poules4Meilleur1 extends Strat4Poules {
	// 4 Poules et on ne retient que les meilleurs de chaque poule
	// -> possible de faire une sous classe abstraite pour les stratégies où on crée 4 poules
	//		pour éviter duplication code de createGroupStage()
	
	
	public Poules4Meilleur1() {
		super();
	}

	@Override
	public List<Competitor> selectCompetitors(List<League> poules) {
		List<Competitor> res = new ArrayList<Competitor>();
		for(League poule : poules) {
			Map<Competitor,Integer> ranked = poule.ranking();
			for (Map.Entry<Competitor,Integer> c : ranked.entrySet()) {
				res.add(c.getKey());
				break;
			}
		}
		return res;
	}

}

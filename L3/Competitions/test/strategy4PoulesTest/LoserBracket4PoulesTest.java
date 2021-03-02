package strategy4PoulesTest;



import competition.Strategy;
import strategy4Poules.LoserBracket4Poules;
import strategyTest.Strat4PoulesTest;

public class LoserBracket4PoulesTest extends Strat4PoulesTest {

	@Override
	protected Strategy create() {
		return new LoserBracket4Poules();
	}

	

}

package strategy4PoulesTest;



import competition.Strategy;
import strategy4Poules.Poules4Meilleur1;
import strategyTest.Strat4PoulesTest;

public class Poules4Meilleur1Test extends Strat4PoulesTest {

	@Override
	protected Strategy create() {
		return new Poules4Meilleur1();
	}



}

package competition;

import java.util.List;

import cTypes.League;
import exception.InvalidNbOfCompetitorsException;

public abstract class Strategy {

	/**
	 * selectionne les competiteurs qui iront au tournois 
	 * est determiné par la stratégie 
	 * ex : loserBracket fait aller les plus nuls au tournois
	 * @param poules les poules jouées
	 * @return les competiteurs qui sont choisis pour aller au tournois
	 */
	public abstract List<Competitor> selectCompetitors(List<League> poules);

	/**
	 * Crée les poules d'un master 
	 * @param comp liste des competiteurs qui appartiendront aux poules 
	 * @return la liste des leagues qui correspondent aux poules du master
	 * @throws InvalidNbOfCompetitorsException s'il n'y a pas un nombre valide de competiteurs pour les leagues
	 */
	public abstract List<League> createGroupStage(List<Competitor> comp) throws InvalidNbOfCompetitorsException;

}
 
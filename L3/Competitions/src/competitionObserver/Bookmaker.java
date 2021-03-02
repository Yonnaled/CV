package competitionObserver;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import competition.Competitor;

public class Bookmaker implements CompetitionObserver{
	/**
	 * Bookmaker qui associe des cotes à chaque joueur pour les paris d'une competition
	 */
	private Map<Competitor,Integer> cotes;
	
	public Bookmaker(List<Competitor> l) {
		this.cotes = new HashMap<Competitor,Integer>();
		for (Competitor c : l) {
			this.cotes.put(c, 10);
		}
	}
	
	@Override
	public void react(Competitor c1, Competitor c2) {
		String affichage = "Victoire de "+c1+" (côte "+this.cotes.get(c1);
		affichage = affichage + ") face à "+c2+" (côte "+ this.cotes.get(c2)+"). ";
		
		if (this.cotes.get(c1) != 1) {
			this.baisseCote(c1);
			affichage = affichage + "La côte de "+c1+" passe à "+this.cotes.get(c1); 
		}
		else affichage = affichage + "La côte de "+c1+" reste à 1, "; 
		
		this.augmenteCote(c2);
		
		affichage = affichage + ", celle de "+c2+" passe à "+this.cotes.get(c2); 
		
		System.out.println(affichage);
	}
	
	/**
	 * Augmente la cote du joueur c (augmente de 1 la valeur associée à la clé c dans this.cotes)
	 * @param c Competiteur qui va voir sa cote augmenter suite à une défaite
	 */
	private void augmenteCote(Competitor c) {
		this.cotes.replace(c, this.cotes.get(c) + 1);
	}

	/**
	 * baisse la cote du joueur c (baisse de 1 la valeur associée à la clé c dans this.cotes)
	 * @param c Competiteur qui va voir sa cote baisser suite à une victoire
	 */
	private void baisseCote(Competitor c) {
		this.cotes.replace(c, this.cotes.get(c) - 1);
	}
	
	
}
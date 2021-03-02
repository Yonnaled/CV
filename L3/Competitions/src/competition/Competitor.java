package competition;

public class Competitor {

		private String name;
		private Integer nbPoints;
		
		public Competitor(String competitorName) {
			this.name = competitorName;
			this.nbPoints = 0;
		}

		/**
		 * getter sur nbPoints
		 * @return int le nombre de points qu'a le competiteur
		 */
		public int getPoints() {
			return this.nbPoints;
		}


		/**
		 * getter sur name
		 * @return String le nom du joueur
		 */ 
		public String getName() {
			return this.name;
		}

		/**
		 * incrémente le nombre de points du competiteur de 1
		 * car ils gagnent 1 point à chaque victoire
		 * on pourra modifier cette methode pour pouvoir ajouter/soustraire plus de points
		 * selon les conditions futures
		 */ 
		public void addPoints() {
			this.nbPoints++;
		}
		
		@Override
		public String toString() {
			return this.getName();
		}
		
		/**
		 * put score to 0
		 */
		public void toZero() {
			this.nbPoints = 0;
		}
}

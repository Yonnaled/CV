<!DOCTYPE html>
<html>
    <head>
        <title>Formulaire Vlille</title>
    	<meta charset="utf-8">
    	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" crossorigin=""/>
  		<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js" crossorigin=""></script>
		<link rel="stylesheet" type="text/css" href="formulaireCSS.css">
    	<script src="VliveImage.js"></script>
  		<script src="carte.js"></script>


    </head>
	<body>
		<header>VLille</header>
	    <div id="carte_campus"></div>
	    <div id="choix">
		    <ul id="listeStations">
		    	<?php
		    		require("lib/verifyParams.php");
		    		require("json.php");
		    		print(listeStations(getData($nomStation,$nomCommune,$nbVelosDispo,$nbPlacesDispo,$service)));
		    	?>
			</ul>
		    <form action="formulaire.php" method="GET" >


			    <label for="nomStation"n>Nom de la station</label>
			    <input class="selection" type="text" id="nomStation" name="nomStation"><br>

			    <label for="nomCommune"n>Nom de la commune</label>
			    <input class="selection" type="text" id="nomCommune" name="nomCommune"><br>


			    <label for="nbVelosDispo">Nombre de VLille disponible(s) minimum</label>
			    <input class="selection" type="number" id="nbVelosDispo" name="nbVelosDispo" value="1"><br>

			    <label for="nbPlacesDispo">Nombre de places libres minimum</label>
			    <input class="selection" type="number" id="nbPlacesDispo" name="nbPlacesDispo" value="1"><br>


			    <label for="service">Service</label>
			    <select class="selection" name="service" id=service>
			    	<option value="EN+SERVICE">En service</option>
			    	<option value="HORS+SERVICE">Hors service</option>
			    	<option value="TOUTES">Toutes</option>
			    </select>


	      		<button type="reset">Effacer</button>
			    <button type="submit" name="valid">Valider</button>

			</form>
		</div>
		<footer> </footer>
	</body>
</html>

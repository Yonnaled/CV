<?php
	function getData($nomStation,$nomCommune,$nbVelosDispo,$nbPlacesDispo,$service){
		if ($service = "TOUTES"){
			$etat="";
		}
		else{
			$etat="&etat=".$service;
		}
		$reponse = (file_get_contents("http://vlille.fil.univ-lille1.fr/?nom=".$nomStation."&commune=".$nomCommune."&nbvelosdispo=".$nbVelosDispo."&nbplacesdispo=".$nbPlacesDispo.$etat));
		$reponsePhp = json_decode($reponse);
		$size = count($reponsePhp);
		$res = [];
		for ($i=0; $i < $size ; $i++) {
	        $a = get_object_vars($reponsePhp[$i]);
		    $fields = get_object_vars($a[fields]);
	        $res[$fields[nom]] = $fields;
		}
		return $res;
		}

	function listeStations($data){
		$res = "";
		foreach ($data as $station => $value) {
			$geo = $value[geo];
			$geoBalise = "[".$geo[0].",".$geo[1]."]";
			$inseeBalise = $value[insee];
			$res .= "<li data-geo=\"".$geoBalise."\" data-velos=\"".$value[nbvelosdispo]."\" data-dispo=\"".$value[nbplacesdispo]."\">". $value[nom] ."</li>";
		}
		return $res;
	}


?>

<?php 


const METHOD = INPUT_GET;

const COMMUNES = ["LILLE",
	"HELLEMMES",
	"MARCQ EN BAROEUL",
	"VILLENEUVE D'ASCQ",
	"ROUBAIX",
	"LAMBERSART",
	"CROIX",
	"TOURCOING",
	"LA MADELAINE",
	"SAINT ANDRE LEZ LILLE",
	"MONS EN BAROEUL",
	"LOMME",
	"WATTRELOS",
	"LOOS",
	"RONCHIN",
	"FACHES-THUMESNIL"];

const SERVICE = ["EN SERVICE",
	"HORS SERVICE",
	"TOUTES"];





  function checkEnum($name,$values,$default = NULL){
    $res = filter_input(METHOD,$name,FILTER_UNSAFE_RAW);
    if($res === NULL){
      if(is_null($default)){
        
      }
      else {
          $res = $default;
      }
    }
    //else if (! in_array($res,$values)){ }
    return $res;
  }


function checkInt($name,$default){
	$res = filter_input(METHOD,$name,FILTER_VALIDATE_INT,['options'=>['default'=>$default,'min_range'=>0]] );
    if($res === NULL){
      if(is_null($default)){
        
      }
      else {
          $res = $default;
      }
    }	
    return $res;
}

function checkEtat($name,$values,$defalut=NULL){
	$res = filter_input(METHOD,$name,FILTER_UNSAFE_RAW);
	if($res===NULL){
		$res=$default;
	}
	return $res;
}

$nomStation = checkEnum('nomStation', STAIONS);
$nomCommune = checkEnum('nomCommune', COMMUNES);
$nbVelosDispo = checkInt("nbVelosDispo",1);
$nbPlacesDispo = checkInt("nbPlacesDispo",1);
$service = checkEtat("service",SERVICE,"TOUTES");



?>
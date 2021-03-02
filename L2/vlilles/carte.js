window.addEventListener('DOMContentLoaded', ()=>{
      // 1 : création
  let maCarte = L.map('carte_campus');

      // 2 : choix du fond de carte
  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '©️ OpenStreetMap contributors'
  }).addTo(maCarte);

  let pointsList = [];
  for (let item of document.querySelectorAll('#listeStations>li')){
    let nom = item.textContent;
    let geoloc = JSON.parse(item.dataset.geo);
    let velos = item.getAttribute("data-velos");
    let places = item.getAttribute("data-dispo");
    nom += "        Vélos disponible : " + velos;
    nom += "        Places disponible : " + places;
    let image =  VliveImage.getInstance(velos,places);
    let marker = L.marker( geoloc, {icon:image.getLeafletIcon()} ).addTo(maCarte);
    marker.addTo(maCarte).bindPopup(nom);
    pointsList.push(geoloc);
    setupListeners(item,marker);
  }


  	if (pointsList.length>0)
    	maCarte.fitBounds(pointsList);

	function setupListeners(item, marker){
	    // item est le noeud DOM d'un élément li (donc une ville de la liste)
	    // marker est le marqueur Leaflet créé pour cette même ville

	    item.addEventListener('click', ()=>{
		    marker.openPopup();
		    setCurrent(item);
		    maCarte.setView(marker.getLatLng(),14);
	    });
	    marker.on("click", ()=>{
	      setCurrent(item);
	      maCarte.setView(marker.getLatLng(),14);

	    });
	// gestion de l'item courant
	{
	  let itemCourant = null;

	  function setCurrent(item){
	      if (itemCourant)
	          itemCourant.classList.toggle('current');
	      itemCourant = item;
	      itemCourant.classList.toggle('current');
	  }
	}

	};

});

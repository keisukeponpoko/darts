var map = new L.Map('map', {center: new L.LatLng(35.676158, 139.736769), zoom: 12});

var roadMutant = L.gridLayer.googleMutant({
  maxZoom: 24,
  type:'roadmap'
}).addTo(map);

var markers = L.markerClusterGroup();

$.getJSON("ajax/detail", function(data) {
  var len = data.length;

  for(var i = 0; i < len; i++) {
    var shop = data[i];
    var title = shop[2];
    var marker = L.marker(new L.LatLng(shop[0], shop[1]), { title: title });
    marker.bindPopup('<a href="shop/' + shop[3] + '/" target="_blank">' + title + '</a>');
    markers.addLayer(marker);
  }

  map.addLayer(markers);
});

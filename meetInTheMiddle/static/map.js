$.getJSON("https://maps.googleapis.com/maps/api/geocode/json?address=skopja&key=AIzaSyCaBLkUO7eDszM2qaxeBeTnR2JAekImnLk", function(data1) {
  $.getJSON("https://maps.googleapis.com/maps/api/geocode/json?address=poprad&key=AIzaSyCaBLkUO7eDszM2qaxeBeTnR2JAekImnLk", function(data2) {
    initMap(data1.results[0].geometry.location, data2.results[0].geometry.location)
  });


});



function findPhoto(city, cb) {

  service = new google.maps.places.PlacesService(map);
  service.textSearch({query : city}, function(data) {
    ref = data[0].reference
    console.log(data[0].photos[0].getUrl({'maxWidth': 500, 'maxHeight': 500}))
    console.log('https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='+ref+'&key=AIzaSyAut7TRhA_DVhsXUQFM0cr1es1lMv_ymDg')
  });








}


function createUserMarker(loc, map) {
  var image = {
    url: 'static/person.png',

    size: new google.maps.Size(71, 71),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(15, 15),
    scaledSize: new google.maps.Size(30, 30)
  }
  var marker = new google.maps.Marker({
    position: loc,
    map: map,
    icon: image
  });
}

function createDestMarker(loc, map) {
  var marker = new google.maps.Marker({
    position: loc,
    map: map
  });
}

function createPath(loc1, loc2, map) {
  var flightPath = new google.maps.Polyline({
    path: [loc1, loc2],
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  flightPath.setMap(map);
}


function initMap(loc1, loc2) {

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: loc1,
    mapTypeControl: false
  });

  createUserMarker(loc1, map)
  createUserMarker(loc2, map)
  createPath(loc1, loc2, map)




}

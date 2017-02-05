




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
  map.objects.push(marker)

}

function createDestMarker(loc, map) {

  var marker = new google.maps.Marker({
    position: loc,
    map: map
  });
  map.objects.push(marker)
  
}
function createPath(loc1, loc2, map) {
  var flightPath = new google.maps.Polyline({
    path: [loc1, loc2],
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });

  map.objects.push(flightPath)

  flightPath.setMap(map);
}

var map = new google.maps.Map(document.getElementById('map'), {
  zoom: 4,
  center : {"lng":0, "lat":50},
  mapTypeControl: false
});
map.objects = []

function clearMap() {
  for(i=0; i<map.objects.length; i++){
    map.objects[i].setMap(null);
}
}

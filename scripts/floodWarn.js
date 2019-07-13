function floodWarn() {
  this.makeFloodMarkers = function(floodLocData, floodMarkers, map) {
    // removes previous flood markers
    this.clearFloodMarkers(floodMarkers);
    // Adds API data Flood warning markers
    var floodMarker;
    for(var i = 0; i < floodLocData.length; i++) {
        var sev = floodLocData[i]['sev'];
        var title = floodLocData[i]['description'];
        var message = floodLocData[i]['message'];
        if(sev >= 4) {
          floodMarker = new google.maps.Marker({
          position: new google.maps.LatLng(parseFloat(floodLocData[i].lat), parseFloat(floodLocData[i].long)),
          map: map,
          title: title,
          severity: sev,
          message: message,
          icon: 'markers/red_markerF.png'
          })
        } else if(sev >= 3) {
          floodMarker = new google.maps.Marker({
          position: new google.maps.LatLng(parseFloat(floodLocData[i].lat), parseFloat(floodLocData[i].long)),
          map: map,
          title: title,
          severity: sev,
          message: message,
          icon: 'markers/orange_markerF.png'
          })
        } else {
          floodMarker = new google.maps.Marker({
          position: new google.maps.LatLng(parseFloat(floodLocData[i].lat), parseFloat(floodLocData[i].long)),
          map: map,
          title: title,
          severity: sev,
          message: message,
          icon: 'markers/yellow_markerF.png'
          })
        }
        floodMarkers.push(floodMarker);
      }
    return floodMarkers;
  }


  this.clearFloodMarkers = function(floodMarkers) {
    console.log("clearing floodMarkers");
    for(var i=0; i<floodMarkers.length; i++) {
      floodMarkers[i].setMap(null);
    }
  }
}

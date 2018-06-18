
console.log(data.length);
var map, heatmap;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lng: -74.0060, lat: 40.7128},
        zoom: 7
    });
    
    heatmap = new google.maps.visualization.HeatmapLayer({
	data: getPoints(),
	map: map
    });
 
}


function setHeatmap() {
    var gradient = [
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 0, 255, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
    ]
    heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
    heatmap.set('radius', heatmap.get('radius') ? null : 200);
}

function getPoints(){
    points = []
    for (var i=0; i<data.length; i++){
	element = new google.maps.LatLng(data[i][0], data[i][1]);
	//console.log(element);
	points.push( element );
    }
    //points = [ new google.maps.LatLng(43.02143,-76.197701) ]
    console.log("GETPOINTS");
    //console.log(points);
    return points;
    
}


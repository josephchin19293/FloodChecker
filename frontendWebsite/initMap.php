<?php
    $returnJson = [];

    $dbc = mysqli_connect("dragon.kent.ac.uk","ajh203","li3serv","ajh203");
    //Get middle
    $query = "SELECT MIN(dataLatitude) as minLat , MAX(dataLatitude) as maxLat , Min(dataLongitude) as minLong , MAX(dataLongitude) as maxLong FROM SensorData";
    $result = mysqli_query($dbc,$query) or die("Failed to query database");
    $row = mysqli_fetch_row($result);
    $latMiddle = $row[0] + (($row[1]-$row[0])/2);
    $longMiddle = $row[2] + (($row[3]-$row[2])/2);
    //Get most recent results for sensors
    $query = "SELECT DISTINCT(sensor) as sensor FROM SensorData";
    $result = mysqli_query($dbc,$query) or die("Failed to query database");
    $sensors = [];
    while($row = mysqli_fetch_array($result)) {
        $sensors[] = $row['sensor'];
    }
    //print_r($sensors);
    $mostRecentReadings = [];
    $allReadings = [];
    for($i = 0; $i< count($sensors);$i++) {
        $reading = [];
        $query = "SELECT * FROM SensorData where sensor='".$sensors[$i] ."' ORDER BY dataId DESC";
        $result = mysqli_query($dbc,$query) or die("Failed to query database");
        $row = mysqli_fetch_array($result);
        //print_r($row);
        $reading['sensor'] = $row['sensor'];
        $reading['value'] = $row['dataValue'];
        $reading['latitude'] = $row['dataLatitude'];
        $reading['longitude'] = $row['dataLongitude'];
        $reading['timestamp'] = $row['dataTimeStamp'];
        $mostRecentReadings[] = $reading;
        $sensorBaseData['sensor'] = $row['sensor'];
        $sensorBaseData['latitude'] = $row['dataLatitude'];
        $sensorBaseData['longitude'] = $row['dataLongitude'];
        
        $query = "SELECT * FROM SensorData where sensor='".$sensors[$i] ."' ORDER BY dataId ASC";
        $result = mysqli_query($dbc,$query) or die("Failed to query database");
        while($row = mysqli_fetch_array($result)) {
            $smallreading['value'] = $row['dataValue'];
            $smallreading['timestamp'] = $row['dataTimeStamp'];
            $sensorBaseData['readings'][] = $smallreading;
            $smallreading = null;
        }
        $allReadings[] = $sensorBaseData;
        $sensorBaseData = null;
        
    }
    $returnJson['mostRecentReadings'] = $mostRecentReadings;
    $returnJson['allReadings'] = $allReadings;
    //Get all values for each sensor

    $returnJson['mapCenter'] = ['long'=>$longMiddle,'lat'=>$latMiddle];
    echo json_encode($returnJson);
?>
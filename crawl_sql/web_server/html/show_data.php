<?php
ini_set('display_errors', 1);
// Create connection
$con=mysqli_connect("mysql","root","secret","Temperature");
 
// Check connection
if (mysqli_connect_errno())
{
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
 
// Select all of our stocks from table 'stock_tracker'
//$sql = "SELECT Time, Temp FROM temperature where Station='Seoul' and Time like '%:00:%' order by Time desc limit 20";
$sql = "SELECT Time, Temp FROM temperature where Station='Seoul' order by Time desc limit 20";

// Confirm there are results
if ($result = mysqli_query($con, $sql))
{
 // We have results, create an array to hold the results
        // and an array to hold the data
 $resultArray = array();
 $tempArray = array();

 // Loop through each result
 while($row = $result->fetch_object())
 {
 // Add each result into the results array
     $tempArray = $row;
     array_push($resultArray, $tempArray);
 }

 // Encode the array to JSON and output the results
 echo json_encode($resultArray);
}

// Close connections
mysqli_close($con);
?>

<?php
ini_set('display_errors', 1);

$servername = "127.0.0.1";
$username = "root";
$password = "root";

// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (mysqli_connect_errno())
{
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else{
  echo "connected!";
}
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

echo "connected";

// Create database
$sql = "CREATE DATABASE testPhp";
if (mysqli_query($conn, $sql)) {
  echo "Database created successfully";
} else {
  echo "Error creating database: " . mysqli_error($conn);
}

mysqli_close($conn);
?> 

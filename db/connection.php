<?php
    // Define the database credentials
    $host = "hostname";
    $username = "username";
    $password = "password";
    $database = "database";

    // Connect to the database
    $conn = new mysqli($host, $username, $password, $database);

    // Check if the connection was successful
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
?>


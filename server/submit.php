<?php
    // Include the database connection file
    require_once '../db/connection.php';

    // check if the form has been submitted
    if(isset($_POST['input'])) {
        // Get the user input
        $input = $_POST['input'];

        // Insert the input into the database
        $query = "INSERT INTO inputs (input) VALUES ('$input')";
        $conn->query($query);

        // Pass the input to the API
        $response = file_get_contents('API URL' . $input);

        // Return the response in JSON format
        echo json_encode(array("response" => $response));
    }

    // check if the form has been submitted
    if(isset($_POST['name']) && isset($_POST['email']) && isset($_POST['occupation']) && isset($_POST['role'])) {
        // Get the user input
        $name = $_POST['name'];
        $email = $_POST['email'];
        $occupation = $_POST['occupation'];
        $role = $_POST['role'];

        // Insert the input into the database
        $query = "INSERT INTO waitlist (name, email, occupation, role) VALUES ('$name', '$email', '$occupation', '$role')";
        $conn->query($query);

        // Return a message to confirm that the data has been inserted
        echo json_encode(array("response" => "Data inserted successfully"));
?>

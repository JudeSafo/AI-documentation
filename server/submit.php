<?php
    // Include the database connection file
    require_once '../db/connection.php';

    // Retrieve the user input from the form
    $userInput = $_POST['userInput'];
    // Create a data array with the user input
    $data = array('prompt' => $userInput);
    // Endpoint URL
    $url = 'http://localhost:5000/gpt';
    // Use curl to make a POST request to the API endpoint with the data array
    $options = array(
        'http' => array(
            'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
            'method'  => 'POST',
            'content' => http_build_query($data)
        )
    );
    $context  = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    // Parse the JSON response
    $response = json_decode($result);
    // Use the response data
    echo $response->text;

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

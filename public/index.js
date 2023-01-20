// Handle the click event on the Join Waitlist button
document.getElementById("join-waitlist").addEventListener("click", function(){
    document.getElementById("join-waitlist-form").style.display = "block";
    window.scrollTo(0,document.body.scrollHeight);
});

// Handle the form submission
var form = document.querySelector("form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    var formData = new FormData(form);
    var input = document.getElementById("input").value;
    var file = document.getElementById("file").files[0];

    // Send a post request to the server
    var request = new XMLHttpRequest();
    request.open("POST", "submit.php", true);
    request.onload = function() {
        if (request.status === 200) {
            // Parse the response
            var response = JSON.parse(request.response);

            // Handle the response
            if (response.response === "Data inserted successfully") {
                // Call the API
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "https://api.example.com", true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.onreadystatechange = function() {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        // Get the response from the API
                        var apiResponse = JSON.parse(xhr.response);

                        // Update the response div with the API response
                        document.getElementById("response").innerHTML = apiResponse;
                    }
                };
                var data = JSON.stringify({ input: input, file: file });
		xhr.send(data);
                alert("Your data has been submitted, thank you for joining the waitlist!");
            } else {
                alert("An error occurred, please try again later.");
            }
        }
    };
    request.send(formData);
});


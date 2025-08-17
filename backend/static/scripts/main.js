/*jshint esversion: 6 */

let submit_button = document.getElementById("register_button");
if (submit_button){
    submit_button.onclick = function addNewUser() {

        let username = document.getElementById("register_username").value;
        let email = document.getElementById("register_email").value;
        let password = document.getElementById("register_password").value;
        
        if (!username || !email || !password) {
            alert("Please fill in all fields");
            return;
        }
        
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        fetch('/api/user', {
                body: JSON.stringify(data),
                method: 'POST',
                headers: new Headers({
                    'Content-Type': 'application/json'
                })
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (myJson) {
                console.log(myJson);
                if (myJson.message && myJson.message.includes("created")) {
                    alert("User registered successfully! Please login.");
                    window.location.href = "/login";
                } else if (myJson.error) {
                    alert("Registration failed: " + myJson.error);
                } else {
                    alert("Registration failed: " + (myJson.message || "Unknown error"));
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
                alert("Registration failed: Network error");
            });
    };
}

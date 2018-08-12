/*jshint esversion: 6 */

let submit_button = document.getElementById("register_button");
if (submit_button){
    submit_button.onclick = function addNewUser() {

        let username = document.getElementById("register_name").value;
        let email = document.getElementById("register_email").value;
        let password = document.getElementById("register_password").value;
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
                location.reload()
                return response.json();
            })
            .then(function (myJson) {
                console.log(myJson);
            });
    };
}

let login_button = document.getElementById("login_button");
if (login_button) {
    login_button.onclick = () => {
        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        data = {
            "email": email,
            "password": password
        };
        fetch('/login', {
                body: JSON.stringify(data),
                method: 'POST',
                headers: new Headers({
                    'Content-Type': 'application/json'
                })
            }).then(() => {
                window.location.replace("/");
            });
        };
    }
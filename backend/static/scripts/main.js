/*jshint esversion: 6 */
console.log('hi')

let submit_button = document.getElementById("register_button");
if (submit_button){
    submit_button.onclick = function addNewUser() {

        let username = document.getElementById("username").value;
        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
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
            }).then((server_response) => {
                server_response.json().then((data) => {
                    let jwt_token = data.jwt_token;
                    window.localStorage.jwt_token = data.jwt_token;
                    window.location.replace("/");
                });
            });
        };
    }
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
            }).then((server_response) => {
                server_response.json().then((data) => {
                    let jwt_token = data.jwt_token;
                    window.localStorage.jwt_token = data.jwt_token;
                    setCookie('jwt_token', data.jwt_token, 7);
                    window.location.replace("/");
                });
            });
        };
    }

function setCookie(name, value, days) {
    console.log('sett new cookie');
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) {
    document.cookie = name + '=; Max-Age=-99999999;';
}
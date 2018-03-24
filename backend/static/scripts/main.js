console.log('hi')

let submit_button = document.getElementById("register_button");
if (submit_button !== null){
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

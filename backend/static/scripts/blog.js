/*jshint esversion: 6 */

let add_post = document.getElementById("add_post");
  add_post.onclick = function addNewPost() {

      let email = document.getElementById("email").value;
      let title = document.getElementById("post_title").value;
      let content = document.getElementById("post_content").value;

      data = {
          "email": email,
          "title": title,
          "content": content
      }
      fetch('/api/blog_post/create', {
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

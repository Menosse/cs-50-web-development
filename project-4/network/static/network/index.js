// When DOM Loads, add event listener
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#post-form').addEventListener('submit', new_post);
    });

function new_post(){
    event.preventDefault();
    fetch('/compose', {
        method: 'POST',
        body: JSON.stringify({
            post_body: document.querySelector('#post-body').value,
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        document.querySelector('#post-body').value = '';
    })
    .catch(error => {
        console.log("Error", error);
    })
}
// Start with first post
let counter = 1;

// Load 20 posts at time
const quantity = 20;

// When DOM Loads, render first 20 Posts
document.addEventListener('DOMContentLoaded', () =>{
    load();
});


document.addEventListener('click', event =>{
    const element = event.target;
    if(element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'runnnig';
        element.parentElement.addEventListener('animationend', () =>{
            element.parentElement.remove();
        });
    }
});

window.onscroll = () =>{
    if(window.innerHeight + window.scrollY >= document.body.offsetHeight){
        load();
    }
};

// Load next set of posts
function load() {
    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add posts
    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(add_post);
        console.log(start)
        console.log(end)
        });
};

// Add a new post with given contents to DOM
function add_post(contents){
    // Create new post
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `${contents} <button class='hide'>Hide</button>`;
    // Add post to DOM
    document.querySelector('#posts').append(post);
};


// When DOM Loads, add event listener
document.addEventListener('DOMContentLoaded', function(){
    
    //add event listener
    document.querySelector('#post-form').addEventListener('submit', new_post);
    document.querySelector('#following').addEventListener('click', () => load_posts('following'));
    document.querySelector('#all-posts').addEventListener('click', () => load_posts('all'));
    document.querySelector('#user-page').addEventListener('click', () => load_posts('all'));

    //add textarea autogrow effect
    var textarea = document.querySelector('#post-body');
    textarea.value='';
    textarea.addEventListener('keydown', autosize);
    
    //Load all by default
    load_posts('all');
    
    //like buttons
    setTimeout(function(){
        config_like_button()
    },100)
})

function get_user(){
    fetch(`/user`)
    .then(response => response.json())
    .then(result =>{return(result.user) })}


// Like a post and update the front
function like_post(post_id){
    fetch(`/single_post/${post_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            num_likes: post_id
        })
    })
    .catch(error => {
        console.log("Error", error);
    }).then(()=>{
        fetch(`/single_post/${post_id}`)
        .then(response => response.json())
        .then(post =>{
        like_div = document.getElementById(post_id).parentNode.previousSibling
        like_div.innerHTML = `${post.num_likes}`
        })
    })
    if(event.target.innerHTML==='Like!'){
        event.target.innerHTML='Unlike'
    }else{event.target.innerHTML='Like!'}
}

function load_posts(postkind){
    event.preventDefault();
    if(postkind === 'all'){
        document.querySelector('#compose-view').style.display = 'block'
    }if(postkind==='following'){
        document.querySelector('#compose-view').style.display = 'None'
        document.querySelector('#posts-view').style.display = 'block'
    }
    document.querySelector('#posts-view').innerHTML = `<h3>${postkind.charAt(0).toUpperCase() + postkind.slice(1)}</h3>`;
    get_posts(postkind)
}

// Autosize the POST text area
function autosize(){
    var el = this;
    setTimeout(function(){
        el.style.cssText = 'height:auto; padding:0';
        el.style.cssText = 'height:' + el.scrollHeight + 'px';
    },0);
    }

//Make a new post
function new_post(){
    event.preventDefault();
    if(document.querySelector('#post-body').value === ''){
        console.log("Post is empty")
    }else{
        fetch('/compose', {
            method: 'POST',
            body: JSON.stringify({
                post_body: document.querySelector('#post-body').value,
            })
        })
        .then(response => response.json())
        .then(result => {
            document.querySelector('#post-body').value = '';
        })
        .catch(error => {
            console.log("Error", error);
        })
    }
}

function get_posts(postkind){
    fetch(`/posts/${postkind}`)
    .then(response => response.json())
    .then(result =>{
        result.forEach(post => {
            //Create user div
            const user_div = document.createElement('div');
            user_div.className = "user_div col-sm-2";
            user_div.innerHTML = ` ${post.user}`;
            
            //Create post body col
            const post_div = document.createElement('div');
            post_div.innerHTML = `${post.body} ${post.timestamp}`;
            post_div.className = "post_div col-sm";
            
            //Create likes div
            const likes_div = document.createElement('div');
            likes_div.innerHTML = `${post.num_likes}`
            likes_div.className = "likes_div col-sm";
            //Create like button
            const like_button_div = document.createElement('div');
            like_button_div.className = "like_button_div col-sm";
            const like_button = document.createElement("button");
            like_button.id = `${post.id}`;
            like_button.className = "like-button btn btn-primary"
            like_button_div.appendChild(like_button)
            fetch('/user')
            .then(response => response.json())
            .then(result =>{
                if(post.liked_by_user.includes(result.user)){
                    like_button.innerHTML = "Unlike";
                }else {like_button.innerHTML = "Like!";}
            })
            
            
            post_div.appendChild(likes_div)
            post_div.appendChild(like_button_div)

            //Create new Row
            const row_div = document.createElement('div');
            row_div.className = "row";
            row_div.id = "post-row";
            row_div.appendChild(user_div);
            row_div.appendChild(post_div);

            //Append to the DOM
            document.querySelector('#posts-view').appendChild(row_div);
            
        });
    })
    .catch(error =>{
        console.log("Error", error)
    })
}

function config_like_button(){
    document.querySelectorAll(".like-button").forEach(button => {
        console.log(button.id)
        button.onclick = () =>{
            like_post(button.id)
        }

    })
}

// When DOM Loads, add event listener
document.addEventListener('DOMContentLoaded', function(){
    //add event listener
    document.querySelector('#post-form').addEventListener('submit', new_post);
    document.querySelector('#following').addEventListener('click', () => load_posts('following'));
    document.querySelector('#all-posts').addEventListener('click', () => load_posts('all'));
    document.querySelector('#user-page').addEventListener('click', () => load_posts('all'));
    document.querySelectorAll('.like-button').forEach(button=>{
        button.onclick = ()=>{
            console.log('like clicked')
        }
    })

    //add textarea autogrow effect
    var textarea = document.querySelector('#post-body');
    textarea.value='';
    textarea.addEventListener('keydown', autosize);
    
    //Load all by default
    load_posts('all');
    //like buttons
    //config_like_button();
        
    });

document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        console.log(document.querySelectorAll('.like-button'))
        console.log(document.readyState)
    }
    }
      
    
function get_user(){
    fetch(`/user`)
    .then(response => response.json())
    .then(result =>{return(result.user) })}

function like_post(post_id){
    fetch(`/single_post/${post_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            num_likes: post_id
        })
    })
    .catch(error => {
        console.log("Error", error);
    })
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

function autosize(){
    var el = this;
    setTimeout(function(){
        el.style.cssText = 'height:auto; padding:0';
        el.style.cssText = 'height:' + el.scrollHeight + 'px';
    },0);
    }

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
            post_div.innerHTML = `${post.body} ${post.num_likes} ${post.timestamp}`;
            post_div.className = "post_div col-sm";
            
            //Create like button
            const like_button = document.createElement("button");
            like_button.id = `${post.id}`;
            like_button.className = "like-button btn btn-primary"
            like_button.addEventListener('click', () =>{like_post(like_button.id)})
            fetch('/user')
            .then(response => response.json())
            .then(result =>{
                if(post.liked_by_user.includes(result.user)){
                    like_button.innerHTML = "Unlike!";
                }else {like_button.innerHTML = "Like!";}
            })
            post_div.appendChild(like_button)


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
    const buttons = document.getElementsByClassName("like-button")
    console.log(buttons);
    console.log(document.querySelectorAll(".like-button"))

    //fetch('/user')
    //.then(response => response.json())
    //.then(result =>{
    //    if(post.liked_by_user.includes(result.user)){
    //        like_button.innerHTML = "Unlike!";
    //    }else {like_button.innerHTML = "Like!";}
    //})
}
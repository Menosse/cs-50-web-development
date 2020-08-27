// When DOM Loads, add event listener
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#post-form').addEventListener('submit', new_post);
    load_posts();
    });

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
            console.log(result);
            document.querySelector('#post-body').value = '';
        })
        .catch(error => {
            console.log("Error", error);
        })
    }
}

function load_posts(){
    fetch('/posts')
    .then(response => response.json())
    .then(result =>{
        result.forEach(post => {
            //Create user div
            const user_div = document.createElement('div');
            user_div.className = "user_div col-sm-2";
            user_div.innerHTML = ` ${post.user}`;
            
            //Create post body col
            const post_div = document.createElement('div');
            post_div.innerHTML = `${post.body} ${post.num_likes}`;
            post_div.className = "post_div col-sm";
            
            //Create new Row
            const row_div = document.createElement('div');
            row_div.className = "row";
            row_div.appendChild(user_div)
            row_div.appendChild(post_div)
            
            //Append to the DOM
            document.querySelector('#posts-view').append(row_div);
            //document.querySelector('#posts-view').append(post_div);
        });
    })
    .catch(error =>{
        console.log("Error", error)
    })
}
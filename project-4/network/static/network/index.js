
// When DOM Loads, add event listener
document.addEventListener('DOMContentLoaded', function(){
        //post buttons
        setTimeout(function(){
            config_like_button()
            config_edit_button()
            config_save_button()
        },1000)
    
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
    paginator('all')
})


function get_user(){
    fetch(`/user`)
    .then(response => response.json())
    .then(result =>{return(result.user) })
}

function load_posts(postkind,page){
    //event.preventDefault();
    if(postkind === 'all'){
        document.querySelector('#compose-view').style.display = 'block'
    }if(postkind==='following'){
        document.querySelector('#compose-view').style.display = 'None'
        document.querySelector('#posts-view').style.display = 'block'
    }
    document.querySelector('#posts-view').innerHTML = `<h3>${postkind.charAt(0).toUpperCase() + postkind.slice(1)}</h3>`;
    get_posts(postkind,page)
}

function paginator(postkind){
    fetch(`/posts/${postkind}`)
    .then(response => response.json())
    .then(result =>{
        for(i=0;i<result.num_pages;i++){
            const pag_button = document.createElement("button")
            pag_button.innerHTML = `${i+1}`
            pag_button.className = "page-button btn btn-primary"
            const page_num = i+1
            console.log(page_num)
            pag_button.addEventListener('click', () => load_posts(postkind,page_num));
            document.querySelector('#footer').appendChild(pag_button);
        }
    })
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
        }).then(window.location.reload())
    }
}

function get_posts(postkind, page){
    fetch(`/posts/${postkind}?page=${page}`)
    .then(response => response.json())
    .then(result =>{
        result.posts.forEach(post => {
            //Create user div
            const user_div = document.createElement('div');
            user_div.className = "user_div col-sm-2";
            user_div.innerHTML = ` ${post.user} `;
            
            //Create post div
            const post_div = document.createElement('div');
            post_div.className = "post_div col-sm";
            post_div.id = `post_div_${post.id}`

            //Create body div
            const body_div = document.createElement('div');
            body_div.innerHTML = `${post.body} ${post.timestamp}`;
            body_div.className = "body_div col-sm";
            body_div.id = `body_div_${post.id}`
            
            //Create likes div
            const likes_div = document.createElement('div');
            likes_div.innerHTML = `${post.num_likes}`
            likes_div.className = "likes_div col-sm";
            likes_div.id = `likes_div_${post.id}`

            //Create like button and edit button
            const like_button_div = document.createElement('div');
            like_button_div.className = "like_button_div col-sm";
            const like_button = document.createElement("button");
            like_button.id = `${post.id}`;
            like_button.className = "like-button btn btn-primary"
            like_button_div.appendChild(like_button)

            
            
            const edit_div = document.createElement('div');
            const edit_button_div = document.createElement('div')



            fetch('/user')
            .then(response => response.json())
            .then(result =>{
                //create like/unlike button
                if(post.liked_by_user.includes(result.user)){
                    like_button.innerHTML = "Unlike";
                }else {like_button.innerHTML = "Like!";}
                
                //create edit elements
                if(post.user === result.user){
                    // create edit post div
                    
                    edit_div.style.display = "none"
                    edit_div.className = 'edit_div'
        
                    //create edit area
                    const edit_area = document.createElement('TEXTAREA')
                    edit_area.innerHTML = `${post.body}`
                    edit_area.id = `edit_area_${post.id}`
                    edit_area.className = `form-control edit_area`

                    //create save edit button
                    const save_edit_button = document.createElement('button')
                    save_edit_button.innerHTML = "Save"
                    save_edit_button.id = `save_edit_button_${post.id}`
                    save_edit_button.className = "save-edit-button btn btn-primary"
                    
                    //append edit area and button to the DOM
                    edit_div.appendChild(edit_area)
                    edit_div.appendChild(save_edit_button)
                    

                    //create edit button
                    
                    edit_button_div.className = 'edit_button_div'
                    const edit_button = document.createElement('button')
                    edit_button.className = `edit-button btn btn-primary`
                    edit_button.id = `edit_button_${post.id}`
                    edit_button.innerHTML = `Edit Post`
                    edit_button_div.appendChild(edit_button)
                    
                    //append to the DOM
                    
                }
                
            })

            //Create new Row
            const row_div = document.createElement('div');
            row_div.className = "row";
            row_div.id = `${post.id}`;
            row_div.appendChild(user_div);
            row_div.appendChild(post_div);

            //Append to the DOM
            post_div.appendChild(body_div)
            post_div.appendChild(edit_div)
            post_div.appendChild(edit_button_div)
            post_div.appendChild(likes_div)
            post_div.appendChild(like_button_div)

            document.querySelector('#posts-view').appendChild(row_div);
            
        });
    })
    .catch(error =>{
        console.log("Error", error)
    })
    
}

function config_like_button(){
    document.querySelectorAll(".like-button").forEach(button => {
        button.onclick = () =>{
            like_post(button.id)
        }

    })
}

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
        like_div = document.getElementById(`likes_div_${post_id}`)
        like_div.innerHTML = `${post.num_likes}`
        })
    })
    if(event.target.innerHTML==='Like!'){
        event.target.innerHTML='Unlike'
    }else{event.target.innerHTML='Like!'}
}


function config_edit_button(){
    document.querySelectorAll(".edit-button").forEach(button=>{
        
        button.onclick = ()=>{
            edit_post()
        }
    })
}

function edit_post(){
    event.target.parentNode.previousSibling.style.display = "block"
    event.target.parentNode.previousSibling.previousSibling.style.display = "none"
    event.target.parentNode.style.display = "none"
    //target.parentNode.previousSibling.style.display = "block"
}

function config_save_button(){
    document.querySelectorAll(".save-edit-button").forEach(button=>{
        
        button.onclick = ()=>{
            save_edit_post(button.id)
        }
    })
}

function save_edit_post(button_id){
    
    const post_id = document.getElementById(button_id).parentNode.parentNode.parentNode.id
    const content = document.getElementById(button_id).previousSibling.value
    fetch(`/single_post/content/${post_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            post_body: content
        })
    }).catch(error => {
        console.log("Error", error);
    })
    .then(()=>{
        fetch(`/single_post/${post_id}`)
        .then(response => response.json())
        .then(post =>{
        post_div = document.getElementById(`body_div_${post.id}`)
        post_div.innerHTML = `${post.body} ${post.timestamp}`
        })
    })
    
    event.target.parentNode.style.display="none"
    
    event.target.parentNode.previousSibling.style.display = "block"
    
    event.target.parentNode.nextSibling.style.display="block"
}
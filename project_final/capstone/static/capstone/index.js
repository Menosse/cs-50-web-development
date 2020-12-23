document.addEventListener('DOMContentLoaded', function(){

    //document.querySelector('#blog-1').addEventListener('click', () => get_projects());
    get_projects()
    //console.log('loaded')
})

function get_projects(){
    fetch('/list_projects')
    .then(response => response.json())
    .then(result =>{
        const blog_div = document.createElement('div')
        blog_div.className = 'row row-cols-1 row-cols-md-2'
        
        result.projects.forEach(project => {
            const project_div = document.createElement('div');
            project_div.className = `project_div_${project.id} col mb-4`;
            blog_div.appendChild(project_div)

            const card_div = document.createElement('div');
            card_div.className = `card_div_${project.id} card`;
            project_div.appendChild(card_div)

                const card_overlay_div = document.createElement('div');
                card_overlay_div.className = `card_overlay_div_${project.id} view overlay`;
                
                    const overlay_image = document.createElement('img')
                    overlay_image.className = 'card-img-top'
                    overlay_image.src = `${project.main_image}`
                    overlay_image.alt = 'image not found'
                    card_overlay_div.appendChild(overlay_image)

                    const overlay_link = document.createElement('a')
                    overlay_link.className = 'mask rgba-white-slight'
                    overlay_link.src = 'a'
                    card_overlay_div.appendChild(overlay_link)

                card_div.appendChild(card_overlay_div)

                const card_body_div = document.createElement('div')
                card_body_div.className = 'card-body'

                    const card_body_h4 = document.createElement('h4')
                    card_body_h4.className = 'card-title'
                    card_body_h4.innerHTML = `${project.name}`
                    card_body_div.appendChild(card_body_h4)

                    const card_body_p = document.createElement('p')
                    card_body_p.className = 'card-text'
                    card_body_p.innerHTML = `${project.description}`
                    card_body_div.appendChild(card_body_p)

                    const card_body_a = document.createElement('a')
                    card_body_a.className = "btn btn-primary btn-md"
                    card_body_a.href = `${project.id}`
                    card_body_a.innerHTML = 'Read more'
                    card_body_div.appendChild(card_body_a)

                card_div.appendChild(card_body_div)
            
            //console.log(`${project.name}`)
            document.querySelector('#blog_div').appendChild(blog_div)
        });
    }).then(document.querySelector('#blog_div').style.display = 'block')
}
document.addEventListener('DOMContentLoaded', function(){

    //document.querySelector('#blog-1').addEventListener('click', () => get_projects());
    get_projects()
    //console.log('loaded')
    get_project_details()
})

//import BSN from bootstrap-native.esm.min.js;

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

/*
function get_project_details(project_id){
    fetch('/projectphotos/7')
    .then(response => response.json())
    .then(result =>{

        
        var myCarouselInit = new BSN.Carousel('#myCarousel', {
            interval: false,
            pause: false,
            keyboard: false
          });

          var currentActiveItem = myCarouselInit.getActiveIndex();
          console.log(currentActiveItem)

          document.querySelector('#carousel').appendChild(myCarouselInit)
        
        
        const carousel_wrapper = document.createElement('div')
        carousel_wrapper.id = 'carousel-example-1z'
        carousel_wrapper.className = 'carousel slide carousel-fade'

            const carousel_indicator = document.createElement('ol')
            carousel_indicator.className = 'carousel-indicators'
            carousel_indicator.dataset.ride = "carousel"
            
                result.photos.forEach(photo => {
                    const li_object = document.createElement('li')
                    li_object.dataset.target = "carousel-example-1z"
                    li_object.className = 'active'
                    //li_object.dataset.slide = `${index}`
                    carousel_indicator.appendChild(li_object)
                    console.log(photo)
                })
            carousel_wrapper.appendChild(carousel_indicator)
            
            
            const carousel_item_inner_div = document.createElement('div')
            carousel_item_inner_div.className = 'carousel-inner'
            carousel_item_inner_div.role='listbox'
            
                result.photos.forEach(photo => {
                const carousel_item = document.createElement('div')
                carousel_item.className = "carousel-item active"
                carousel_item_inner_div.appendChild(carousel_item)

                    const image_item = document.createElement('img')
                    image_item.className = 'd-block w-100'
                    image_item.src = `${photo.images}`
                    image_item.alt = 'image not found'
                    image_item.appendChild(carousel_item)
                })    


            carousel_wrapper.appendChild(carousel_item_inner_div)
        
        document.querySelector('#carousel').appendChild(carousel_wrapper)
    })

}

*/

/*
<!--Carousel Wrapper-->
<div id="carousel-example-1z" class="carousel slide carousel-fade" data-ride="carousel">
    <!--Indicators-->
    <ol class="carousel-indicators">
    {% for p in photos %}
      <li data-target="#carousel-example-1z" data-slide-to="{{ forloop.counter0 }}" class="{% if forloop.counter0 == 0 %} active {% endif %}"></li>
    {% endfor %}
    </ol>
    <!--/.Indicators-->
    <!--Slides-->
    <div class="carousel-inner" role="listbox">
      {% for p in photos %}
      <div class="carousel-item {% if forloop.counter0 == 0 %} active {% endif %}">
        <img class="d-block w-100" src="{{p.images.url}}"
          alt="First slide">
      </div>
      {% endfor %}
      <!--/First slide-->
    <!--/.Slides-->
    <!--Controls-->
    <a class="carousel-control-prev" href="#carousel-example-1z" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carousel-example-1z" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
    <!--/.Controls-->
  </div>
  */
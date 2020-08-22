function showSection(section){
    fetch(`/section/${section}`)
    .then(response => response.text())
    .then(text =>{
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    })
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function(){
            showSection(this.dataset.section);
        }
    });
});
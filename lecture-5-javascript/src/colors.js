document.addEventListener('DOMContentLoaded',() =>{
    // Change font color
    document.querySelectorAll('button').forEach(button =>{
        button.onclick = () =>{
            document.querySelector("#hello").style.color = button.dataset.color;
        }
    })

    document.querySelector('select').onchange = function(){
        document.querySelector("#hello").style.color = this.value;
    }

});
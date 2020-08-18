if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}

function count(){            
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector("h1").innerHTML = counter;
    localStorage.setItem('counter', counter);   
    /*if (counter % 10 === 0){
        alert(`Count is now ${counter}`);
    }*/
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;    
    document.querySelector("h1").innerHTML = localStorage.getItem('counter');
    //setInterval(count, 1000)
});

function hello(){
    const heading = document.querySelector('h1');
    if (heading.innerHTML==='Hello!'){
        heading.innerHTML='Goodbye!';
    } else {
        heading.innerHTML='Hello!';
    }
}
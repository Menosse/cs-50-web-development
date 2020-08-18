if(!localStorage.getItem('rate')){
    localStorage.setItem('rate', 'USD');
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector("#currency").value = localStorage.getItem('rate');
    document.querySelector('form').onsubmit = () => {
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        .then(response => response.json())
        .then(data => {
            const currency = document.querySelector('#currency').value.toUpperCase();
            localStorage.setItem('rate', currency);
            const rate = data.rates[currency];
            if(rate !== undefined){
                document.querySelector('#result').innerHTML = `1 USD = ${rate.toFixed(3)} ${currency}`;
            } else {
                document.querySelector('#result').innerHTML = `Invalid currency`;
            }
    })
    .catch(error => {
        console.log("Error", error);
    });
        return false;
    }
});
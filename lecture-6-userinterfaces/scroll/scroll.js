window.onscroll = () => {
if(window.innerHeight + window.scrollY >= document.body.offsetHeight){
    document.querySelector('body').style.background = "green"
} else{
    document.querySelector('body').style.background = "white"
    }
}
window.addEventListener('DOMContentLoaded', (event) => {
    jQuery('.navFixa').css("background-color", "");
    jQuery(window).scroll(function() {
        if (jQuery(window).scrollTop() > 10) {
            jQuery('.navFixa').css("background-color", "#0E1122");
            jQuery('.navFixa a:hover').css("");
        } else {
            jQuery('.navFixa').css("background-color", "");
            jQuery('.navFixa a:hover').css("");
        }
    });
});

let botao = document.querySelector('.refresh');
botao.onclick = function refresh(){
    window.history.back();
}

function dropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}
  
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
    let myDropdown = document.getElementById("myDropdown");
        if (myDropdown.classList.contains('show')) {
            myDropdown.classList.remove('show');
        }
    }
}

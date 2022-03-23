window.addEventListener("load", function(){
    setTimeout(
        function open(event){
            document.querySelector(".popup").style.display = "flex";
        },
        500
        )
        navigator.vibrate(2000);
});


document.querySelector("#close").addEventListener("click", function(){
    document.querySelector(".popup").style.display = "none";
    document.querySelector(".pending-card").style.display = "block";
});

document.querySelector("#ok").addEventListener("click", function(){
    document.querySelector(".popup").style.display = "none";
    document.querySelector(".pending-card").style.display = "block";
});
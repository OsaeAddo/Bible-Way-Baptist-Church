var transaction_container = document.getElementsByClassName('transaction')
var transaction_details_container = document.getElementsByClassName('transaction-details-container')

const up_arrow = document.querySelector('#up-arrow')
const down_arrow = document.querySelector('#down-arrow')

var i;

function toggleContent(){
    this.classList.toggle('active');
    var content = this.nextElementSibling;
    if (content.style.display === "block"){
        content.style.display = "none"
    }else {
    content.style.display = "block"
    }
}

for (i=0; i<transaction_container.length; i++){
    transaction_container[i].addEventListener("click", toggleContent);
}


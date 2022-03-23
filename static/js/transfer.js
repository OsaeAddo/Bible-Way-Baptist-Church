const submit = document.querySelector('.continue')
const popup_confirmation = document.querySelector('.popup-confirmation')
const closeButton = document.querySelector('.close-button')


var selectTransferType = document.querySelector('.transfer-type')
const bank_container = document.querySelector('.bank-container')
var i;

function toggleConfirmation(){
    popup_confirmation.classList.toggle('show-confirmation')
}

function toggleBank(){
    bank_container.style.display = "grid"
}


selectTransferType.addEventListener('change', toggleBank)
submit.addEventListener('click', toggleConfirmation)
closeButton.addEventListener('click', toggleConfirmation)
const modal_content = document.querySelector('.modal-content')

const q1_input = document.getElementById('q1-input')
const q2_input = document.getElementById('q2-input')
var ans_btn = document.getElementById('ans_btn')

const error_msg = document.querySelector('.error-msg')

function enableBtn() {
    ans_btn.disabled = false
    ans_btn.classList.remove('disabled-submit-btn')
}
function disableBtn() {
    ans_btn.disabled = true
    ans_btn.classList.add('disabled-submit-btn')
}


function checkAnswer(){
    /*
    1. disable if either is wrong or empty
    2. enable if both are right
    */
    q1_input.addEventListener('input', (e) => {
        q2_value = q2_input.value;
        if (q1_input.value.trim().toLowerCase() === "cherry") {
            q1_input.classList.add('green-border')
            q1_input.classList.remove('red-border')

            if (q2_value.trim().toLowerCase() === "ohio") {
                enableBtn()
            } else {
                disableBtn()
            }
        } else {
            disableBtn()
            q1_input.classList.remove('green-border')
            q1_input.classList.add('red-border')
        }
    })

    q2_input.addEventListener('input', (e) => {
        q1_value = q1_input.value;
        if (q2_input.value.trim().toLowerCase() === "ohio") {
            q2_input.classList.add('green-border')
            q2_input.classList.remove('red-border')

            if (q1_value.trim().toLowerCase() === "cherry") {
                enableBtn()
            } else {
                disableBtn()
            }
        } else {
            disableBtn()
            q2_input.classList.remove('green-border')
            q2_input.classList.add('red-border')
        }
    })    

}

checkAnswer()

window.addEventListener('load', e => {
    disableBtn()
})
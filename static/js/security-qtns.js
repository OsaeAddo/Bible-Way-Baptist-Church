const q1_input = document.getElementById('q1-input')
const q2_input = document.getElementById('q2-input')
var ans_btn = document.getElementById('ans_btn')

const error_msg = document.querySelector('.error-msg')


function checkAnswer(){
    if (q1_input.value.trim().toLowerCase() !== "cherry"){
        error_msg.style.display = "block";
        ans_btn.disabled = true
        ans_btn.style.background = "gray";
        console.log("Wrong answer")
    }else{
        error_msg.style.display = "none";
        ans_btn.disabled = false;
        ans_btn.style.background = "var(--primary)";
    }

    if (q2_input.value.trim().toLowerCase() !== "ohio"){
        error_msg.style.display = "block";
        ans_btn.disabled = true
        ans_btn.style.background = "gray";
        console.log("Wrong answer")
    }else{
        error_msg.style.display = "none";
        ans_btn.disabled = false;
        ans_btn.style.background = "var(--primary)";
    }
}


ans_btn.addEventListener('click', checkAnswer)
let display = document.getElementById("display");
let answer = document.getElementById("answer")

function addToDisplay(value) {
    display.value += value;
}

function deletePrevious(){
display.value = display.value.toString().slice(0,-1)
}

function clearDisplay() {
    display.value = "";
    answer.value = "";
}

function calculate() {
    try {
        answer.value = eval(display.value);
    } catch (error) {
        answer = "Error";
    }
}


function ansValue() {
    display.value = "";
    return answer.value
}
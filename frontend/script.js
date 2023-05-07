let display = document.getElementById("display");

function addToDisplay(value) {
    display.value += value;
}

function deletePrevious(){
display.value = display.value.toString().slice(0,-1)
}

function clearDisplay() {
    display.value = "";
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = "Error";
    }
}
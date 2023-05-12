let display = document.getElementById("display");
let answer = document.getElementById("answer");
let mode = document.getElementById("mode-btn")

function addToDisplay(value) {
    display.value += value;
}

function deletePrevious(){
    display.value = display.value.toString().slice(0,-1);
}

function calculate() {
    try {
        answer.value = eval(display.value);
    } catch (error) {
        display = "Error";
    }
}

function ansValue() {
    display.value = "";
    return answer.value
}

let mode_text = 
`1: COMP            2: CMPLX 
3: STAT             4: BASE-IN
5: EQN              6: MATRIX
7: TABLE            8: VECTOR` 

function clsreen() {
    display.value = "";
    answer.value = ""; 
}

function displayMode() {
    
    display.style.textAlign = "center";
    display.style.fontSize = '20px';
    display.value = mode_text    
}
let modeOn = false;

function clearDisplay() {
    clsreen() 
    display.style.textAlign = "right";
    display.style.fontSize = '30px'; 
}

function toggleMode() {
  if (modeOn) {
    clearDisplay();
    modeOn = false;
  } else {
    displayMode();
    modeOn = true;
  }
}
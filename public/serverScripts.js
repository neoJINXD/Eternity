// Eslint check disabled here since the functions are used within the index.html file

// function to add character based on what button was pressed
/* eslint-disable-next-line */
function addToExpression(toInsert) {
  const textField = document.getElementById('resultInput');
  const oldText = textField.value;
  let caretPosition = textField.selectionStart;
  const newText = oldText.substring(0, caretPosition)
                    + toInsert + oldText.substring(caretPosition);
  textField.value = newText;
  caretPosition += toInsert.length;
  textField.setSelectionRange(caretPosition, caretPosition);
  textField.focus();
}

// function to clear the input field
/* eslint-disable-next-line */
function clearInput() {
  document.getElementById('resultInput').value = '';
}

// function to delete the last character inputted
/* eslint-disable-next-line */
function del() {
  const str = document.getElementById('resultInput').value;
  document.getElementById('resultInput').value = str.substring(0, str.length - 1);
}

// function to delete the datalist
/* eslint-disable-next-line */
function clr() {
  document.getElementById('browserList').innerHTML = '';
}

// function to send a request to node to run the python command
// for calculating the result of the expression
/* eslint-disable-next-line */
async function calc() {  
  // getting the data from which button is selected
  // console.log(document.getElementsByClassName('selected'));
  const arr = document.getElementsByClassName('selected');
  const firstButton = arr[0];
  const secondButton = arr[1];

  const rad = firstButton.id === 'rad';
  const bin = secondButton.id === 'bin';

  // console.log(`Calculation is rad: ${rad} and bin: ${bin}`);

  // forming the input that will be submitted for calculation
  const input = {
    expression: document.getElementById('resultInput').value,
    is_rad: rad,
    is_binary: bin,
  };
  // document.getElementById('equation').innerHTML = `> ${input.expression}`;

  const dlist = document.getElementById('browserList');
  const option = document.createElement('option');
  option.value = document.getElementById('resultInput').value;
  dlist.appendChild(option);

  // calls node to perform the calculation over the route
  const response = await fetch('http://localhost:3000/math', {
    method: 'POST',
    body: JSON.stringify(input),
    headers: {
      'content-type': 'application/json',
    },
  });
  const json = await response.json();

  // Sets the answer in the input text
  document.getElementById('resultOutput').value = `= ${json.answer}`;
  // document.getElementById('resultInput').value = '';
}

document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('resultInput');

  // Execute a function when the user releases a key on the keyboard
  input.addEventListener('keyup', (event) => {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
      event.preventDefault();
      calc();
    }
  });
}, false);

// function for flipping the styles to show which mode is selected
/* eslint-disable-next-line */
function flipSelected(first, second) {
  document.getElementById(first).className = 'selected';
  document.getElementById(second).className = 'operation';
}

// This function is based off: https://www.codeproject.com/Questions/851789/Link-button-onclick-open-pdf-file-in-new-tab
/* eslint-disable-next-line */
function openHelp() {
  // Use the commented out code below for testing until this is pushed to the master branch
  // window.open('https://github.com/neoJINXD/Eternity/blob/UserGuide/User_Guide.pdf');
  window.open('https://github.com/neoJINXD/Eternity/blob/master/User_Guide.pdf');
}

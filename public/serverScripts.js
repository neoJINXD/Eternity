// Eslint check disabled here since the functions are used within the index.html file

// function to add character based on what button was pressed
/* eslint-disable-next-line */
function addToExpression(toInsert) {
  const textField = document.getElementById('resultInput');
  const oldText = textField.value;
  const carretPosition = textField.selectionStart;
  const newText = oldText.substring(0, carretPosition)
                    + toInsert + oldText.substring(carretPosition);
  textField.value = newText;
  textField.selectionStart = carretPosition + length(toInsert);
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
  // gets the input from the textbox
  const input = { expression: document.getElementById('resultInput').value,is_rad: document.getElementById('angleMode').checked };
  document.getElementById('equation').innerHTML = `> ${input.expression}`;

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
  document.getElementById('answer').innerHTML = `= ${json.answer}`;
  document.getElementById('resultInput').value = '';
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

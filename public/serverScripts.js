// function to add character based on what button was pressed
function addToExpression(i){
    document.getElementById('resultInput').value = document.getElementById('resultInput').value + i;
}

// function to clear the input field
function clearInput() { 
    document.getElementById('resultInput').value = '' 
}

// function to delete the last character inputted
function del() { 
    str = document.getElementById('resultInput').value;
    document.getElementById('resultInput').value = str.substring(0, str.length - 1)
}

// function to delete the datalist
function clr() {
    document.getElementById('browserList').innerHTML = '';
}

// function to send a request to node to run the python command for calculating the result of the expression
async function calc() {
    // gets the input from teh textbox
    const input = { expression: document.getElementById('resultInput').value };
    document.getElementById('equation').innerHTML = `> ${input.expression}`;

    dlist = document.getElementById('browserList');
    option = document.createElement('option');
    option.value = document.getElementById('resultInput').value;
    dlist.appendChild(option);

    // calls node to perform the calculation over the route
    const response = await fetch(`http://localhost:3000/math`, {
        method: 'POST',
        body: JSON.stringify(input),
        headers: {
            'content-type': 'application/json'
        }
    });
    const json = await response.json();

    // Sets the answer in the input text
    document.getElementById('answer').innerHTML = `= ${json.answer}`;
    document.getElementById('resultInput').value = '';
}
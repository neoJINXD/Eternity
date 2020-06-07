function calc() {
    const python = require('python-shell');
    const path = require('path');

    var input = document.getElementById('resultInput').value;

    document.getElementById('equation').innerHTML = `> ${input}`;

    console.log('my inpit: ', input);

    const option = {
        args: [input]
    };


    const pyshell = new python('calculate.py', { args: [input] });

    pyshell.on('message', (msg) => {
        console.log(msg);
        let result = msg;
        document.getElementById('answer').innerHTML = `= ${result}`;
        document.getElementById('resultInput').value = '';
    }); 
}

// function to add character based on what button was pressed
function addToExpression(i){
    document.getElementById('resultInput').value = document.getElementById('resultInput').value + i;
}

// function to clear the input field
function clearInput() { document.getElementById('resultInput').value = '' }

// function to delete the last character inputted
function del() { 
    str = document.getElementById('resultInput').value;
    document.getElementById('resultInput').value = str.substring(0, str.length - 1)
}
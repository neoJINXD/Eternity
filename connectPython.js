function calc() {
    const python = require('python-shell');
    const path = require('path');

    var input = document.getElementById('resultInput').value;

    console.log('my inpit: ', input);
    result = '';

    option = {
        args: [input]
    };


    const pyshell = new python('calculate.py', { args: [input] });

    pyshell.on('message', (msg) => {
        console.log(msg);
        result = Number(msg);
        document.getElementById('resultInput').value = result;
    }); 
}
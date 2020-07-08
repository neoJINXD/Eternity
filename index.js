const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.json());

app.get('/', (req, res) => {
    res.send('yes');
});

app.post('/math', (req, res) => {
    //do python math here
    const python = require('python-shell');
    const path = require('path');

    var input = req.body.expression;

    console.log('my inpit: ', input);
    result = '';

    option = {
        args: [input]
    };


    const pyshell = new python('calculate.py', { args: [input] });

    pyshell.on('message', (msg) => {
        //console.log(msg);
        result = Number(msg);
        //document.getElementById('resultInput').value = result;
        res.status(200);
        res.send({ answer: msg });
    }); 
    
});

app.listen(PORT, () => console.log(`Listening on localhost:${PORT}`));
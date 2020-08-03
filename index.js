const express = require('express');
const python = require('python-shell');
// const fs = require('fs');
const path = require('path');

const { execSync } = require('child_process');

const reqPath = path.join(__dirname, '/requirements.txt');

execSync(`pip3 install -r "${reqPath}"`, (error, stdout, stderr) => {
  if (error) {
    /* eslint-disable-next-line */
    console.log(`error: ${error.message}`);
    return;
  }
  if (stderr) {
    /* eslint-disable-next-line */
    console.log(`stderr: ${stderr}`);
    /* eslint-disable-next-line */
    return;
  }
  // console.log(`stdout: ${stdout}`);
});

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.json());

app.get('/', (req, res) => {
  res.send('yes');
});

app.post('/math', (req, res) => {
  // do python math here
  // const python = require('python-shell');
  const input = req.body.expression;
  const isRad = req.body.is_rad;
  const isBinary = req.body.is_binary;
  // console.log('my input: ', input);

  const option = {
    args: [input, isRad, isBinary],
    // args: [input, isRad, isBinary, isBinaryInput],
  };

  // TODO change to always listening python shell instead of creating and deleting everytime
  const pyPath = path.join(__dirname, '/calculate.py');
  /* eslint-disable-next-line */
  const pyshell = new python(pyPath, option);

  pyshell.on('message', (msg) => {
    res.status(200);
    res.send({ answer: msg });
  });
});

/* eslint-disable-next-line */ // Disabled for console log
app.listen(PORT, () => console.log(`Listening on localhost:${PORT}`));
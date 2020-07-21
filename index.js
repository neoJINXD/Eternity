const express = require('express');
const python = require('python-shell');

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
  };

  // TODO change to always listening python shell instead of creating and deleting everytime
  /* eslint-disable-next-line */
  const pyshell = new python('calculate.py', option);

  pyshell.on('message', (msg) => {
    res.status(200);
    res.send({ answer: msg });
  });
});

/* eslint-disable-next-line */ // Disabled for console log
app.listen(PORT, () => console.log(`Listening on localhost:${PORT}`));
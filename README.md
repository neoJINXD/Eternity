# Eternity

## Project for COMP 354

This Project consists of making a calculator with the goal of solving transcendental functions without using existing math libraries.

Information on team organization, tech stack, and the user guide can be found on [our wiki](https://github.com/neoJINXD/Eternity/wiki).

---

### How to Run

#### Prerequisites

[Requires Python 3.8 installed locally](https://www.python.org/downloads/)

[Requires nodejs installed locally](https://nodejs.org/en/)

#### Running the dev versions

```bash
// installs the needed python packages
pip install -r requirements.txt

// installs the node dependencies
npm install

// runs the web app on https://localhost:3000/
npm start

// runs the electron app
npm run electron
```

When running electron, the window will open automatically, but for the web app, the web page must be loaded manually

### Development

Please consult [our wiki](https://github.com/neoJINXD/Eternity/wiki) for a list of technologies used.

#### Testing

Test suites are defined using the `unittest` python library and found in the [/tests](/tests) folder:

```bash
//run tests from the root folder
python -m unittest
```

Be sure to add unit tests for any additional code and cover edge cases!

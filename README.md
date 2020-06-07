# Eternity

## Project for COMP 354

This Project consists of making a calculator with the goal of solving transcendental functions without using existing math libraries.

Information on team organization, tech stack, and the user guide can be found on [our wiki](https://github.com/neoJINXD/Eternity/wiki).

---

### How to Run

#### Prerequisites

[Requires nodejs installed locally](https://nodejs.org/en/)

#### Running the dev versions

```bash

// installs the dependencies
npm install

// runs the web app
npm start

// runs the electron app
npm run electron
```

The application will open in a dedicated desktop window.

### Development

Please consult [our wiki](https://github.com/neoJINXD/Eternity/wiki) for a list of technologies used.

#### Testing

Test suites are defined using the `unittest` python library and found in the [/tests](/tests) folder:

```bash
//run tests from the root folder
python -m unittest
```

Be sure to add unit tests for any additional code and cover edge cases!

const {app, BrowserWindow} = require('electron');
const path = require('path');
const url = require('url');
const pyshell =  require('python-shell');

// Connecting with our web app to use the same API
const express = require('./index'); 

// Initializing the electron app

function createWindow () {
    //express();
    let window = new BrowserWindow({
      width: 800, 
      height: 600,
      webPreferences: {
        nodeIntegration: true
      }
    })

    window.loadURL('http://localhost:3000/');
}


app.on('ready', createWindow)

app.on('window-all-closed', () => {
    //if (process.platform !== 'darwin') {
    app.quit()
    //}
})


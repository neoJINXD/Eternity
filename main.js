/* eslint-disable-next-line */
const { app, BrowserWindow } = require('electron');

// Connecting with our web app to use the same API
require('./index');

// Initializing the electron app

function createWindow() {
  const window = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  window.loadURL('http://localhost:3000/');
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

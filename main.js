const {app, BrowserWindow} = require('electron')
const path = require('path')
const url = require('url')
const pyshell =  require('python-shell');



function createWindow () {
    window = new BrowserWindow({
      width: 800, 
      height: 600
    })
    window.loadFile('calc.html')
    window.setAlwaysOnTop(true)

    
  //   	var python = require('child_process').spawn('python', ['./hello.py']);
	//     python.stdout.on('data',function(data){
  //   	console.log("data: ",data.toString('utf8'));
	// });


  

  //pyshell.run('hello.py',  function  (err, results)  {
  //if  (err)  throw err;
  //console.log('hello.py finished.');
  //console.log('results', results);
  //document.getElementById('resultInput').innerHTML = results;
// });   	
    
}



app.on('ready', createWindow)

app.on('window-all-closed', () => {
    //if (process.platform !== 'darwin') {
    app.quit()
    //}
})


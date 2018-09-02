const { exec } = require('child_process');


function executeTest () {    
    var command = 'ls -lha'
    exec(command, (err, stdout, stderr) => {
        if (err) {
            console.log("Erro ao executar o comando.");
            return;
        }

        console.log('stdout: ', stdout);
        console.log('stderr: ', stderr);        
        if(!stderr){
            console.log('is undefined');
        }
    });

}


var net = require('net');
var server = net.createServer();

server.listen(4723);

server.once('error', function(err) {
  if (err.code === 'EADDRINUSE') {
    // port is currently in use
    console.log(err)
    console.log('Porta em uso!')
  }
});

server.once('listening', function() {
  // close the server if listening doesn't fail
  console.log("A porta não está em uso.")
  server.close();
});


#!/usr/bin/env node
 
/**
 * Module dependencies.
 */
 
var program = require('commander');
 
//configureProgram();

//teste();

//function configureProgram(){
    program
    .version('0.1.0', '-v, --version')
    .option('-i, --input <file>', ' Input .md file')
    .option('-o, --output <directory>', ' Output destination folder')
    .option('-p, --pdf', 'Add pdf')  
    //.option('-c, --cheese [type]', 'Add the specified type of cheese [marble]', 'marble')
    .parse(process.argv);
   
    program.on('--help', function () {
        console.log('  Examples:');
        console.log('');
        console.log('    $ guide-automator -i input.md');
        console.log('    $ guide-automator -i input.md -o output/');
        console.log('    $ guide-automator -i input.md -o output/ -s lightBlue');
        console.log('');
    });
  
//}

function teste(){
    console.log('you ordered a pizza with:');
    console.log('input '+program._name);
    console.log('input '+program.input);
    if(program.pdf)
        console.log('P ', program.pdf);
    //console.log('  - %s cheese', program.cheese);
}

#!/usr/bin/env node
//import lib into global variables
var fs = require('fs');
var Q = require('q');
var net = require('net');
var program = require('commander');
const { exec } = require('child_process');
const { spawn } = require('child_process');
var themeList = ['lightBlue', 'lightOrange'];
var options = {
    debug: false,
    input: "",
    output: ".",
    outlineStyle: "solid red 3px",
    html: true,
    pdf: false,
    /* If true, only image will be export */
    image: false,
    style: 'default',
    autosleep: 200,
    browser: "",
    headless: false,
    window: ""
};

execute();
//setup();

function execute() {
    if (!setup()) {
        process.exit();
    } else {
        checkAppiumStatus(options.port)
            .then(function (appiumStatus) {
                if (appiumStatus)
                    return executeTest(options.input);
            }).then(function (result) {
                if (result && !options.image)
                    return generateHTMLReport(options.output);
            }).then(function (htmlStatus) {
                if (options.pdf && htmlStatus) {
                    return convertOutputToPDF(options.output);
                }
            });
    }
}

function setup() {
    program
        .version('0.1.0', '-v, --version')
        .option('-i, --input <file>', ' Input .md file')
        .option('-o, --output <folder>', ' Output destination folder')
        .option('-P, --pdf', 'Export manual to PDF, default is export for all types')
        .option('-H, --html', 'Export manual to HTML, default is export for all types')
        .option('-I, --image', "Export ONLY manual's image and ignore others types, default is export for all types")
        .option('-s, --style <style.css>', ' Css style to be used in the manual or theme [lightBlue,lightOrange]')
        .option('-p,  --port <port_number>', 'Appium runing port', 4723)

    program.on('--help', function () {
        console.log('  Examples:');
        console.log('');
        console.log('    $ guide-automator -i input.md');
        console.log('    $ guide-automator -i input.md -o output/');
        console.log('    $ guide-automator -i input.md -o output/ -s lightBlue');
        console.log('');
    });

    program.parse(process.argv);

    Object.keys(options)
        .forEach(function (key) {
            options[key] = program[key] || options[key];
            if (options.debug)
                console.log("	" + key + ": " + options[key].toString());
        });

    //if image, others exports type are ignored
    if (options.image)
        options.pdf = options.html = false;

    if (!options.input) {
        console.log('Input file missing. See usage with "' + options._name + ' -h"');
        return false;
    }

    if (!fs.existsSync(options.input) || !fs.lstatSync(options.input).isFile()) {
        console.log('Input is not a file');
        return false;
    }
    if (!fs.lstatSync(options.output).isDirectory()) {
        console.log('Output is not a folder');
        return false;
    }

    return true;

}// setup

function checkAppiumStatus(port = 4723, host = '127.0.0.1') {
    var deferred = Q.defer();
    var server = net.createServer();
    server.listen(port, host);
    server.once('error', function (err) {
        if (err.code === 'EADDRINUSE') {
            // A porta do appium esta em uso
            console.log('Appium process detected runing on ' + host + ':' + port + '.');
            return deferred.resolve(true);
        }
    });

    server.once('listening', function () {
        server.close();
        console.log('No processes was found runing on ' + host + ':' + port + '.');
        return deferred.resolve(false);
    });

    return deferred.promise;
}

function executeTest(inputFile) {
    var deferred = Q.defer();
    var command = 'node ' + inputFile;
    console.log('Executing script[' + inputFile + '].');
    exec(command, (err, stdout, stderr) => {
        if (err) {
            console.log('Something went wrong while running the command[' + command + '].');
            return;
        }

        if (!stderr) {
            deferred.resolve(true);
        } else {
            deferred.resolve(false);
        }
    });
    return deferred.promise;
}

function generateHTMLReport(outPutFolder = '.', outputFile = 'manual.html') {
    var deferred = Q.defer();
    outputHTML = outPutFolder + '/' + outputFile;
    var contents = "<html> <head></head> <body> <h1>Teste</h1> <img src=\"snapshot.png\"/> </body></html>";
    fs.writeFile(outputHTML, contents, function (err) {
        if (err) {
            console.log(err);
            deferred.resolve(false);
        } else {
            deferred.resolve(true);
        }
    });
    return deferred.promise;
}

function convertOutputToPDF(outPutFolder = '.', outputFile = 'manual') {
    console.log('Conversão para PDF!');
    outputPDF = outPutFolder + '/' + outputFile + '.pdf';
    var command = 'wkhtmltopdf ' + outPutFolder + '/' + outputFile + '.html ' + outputPDF;
    exec(command, (err, stdout, stderr) => {
        console.log(stdout);
        console.log(stderr);
        if (err) {
            throw err;
        } else {
            console.log('Arquivo exportado para PDF com sucesso!');
        }
    });
}
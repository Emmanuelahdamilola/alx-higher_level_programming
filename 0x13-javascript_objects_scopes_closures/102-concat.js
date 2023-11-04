#!/usr/bin/node

const fs = require('fs');

const inputFilePathA = process.argv[2];
const inputFilePathB = process.argv[3];
const outputFilePath = process.argv[4];

function concat (inputFileA, inputFileB, outputFile) {
  // Read the content of inputFileA
  fs.readFile(inputFileA, function (err, dataA) {
    if (err) {
      console.log(err.stack);
    } else {
      // Append the content of inputFileA to outputFile
      fs.appendFile(outputFile, dataA, function (err) {
        if (err) {
          console.log(err.stack);
        } else {
          // Read the content of inputFileB
          fs.readFile(inputFileB, function (err, dataB) {
            if (err) {
              console.log(err.stack);
            } else {
              // Append the content of inputFileB to outputFile
              fs.appendFile(outputFile, dataB, function (err) {
                if (err) {
                  console.log(err.stack);
                }
              });
            }
          });
        }
      });
    }
  });
}

concat(inputFilePathA, inputFilePathB, outputFilePath);

#!/usr/bin/node

// Check if there is a command-line argument and store it in 'inputArg'
const inputArg = process.argv[2];

// Check if 'inputArg' is a valid number
if (inputArg && !isNaN(inputArg)) {
  // Convert 'inputArg' to an integer and print it
  console.log('My number: ' + parseInt(inputArg, 10));
} else {
  // If 'inputArg' is not a number, print "Not a number"
  console.log('Not a number');
}


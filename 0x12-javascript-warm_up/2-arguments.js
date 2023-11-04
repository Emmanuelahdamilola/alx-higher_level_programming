#!/usr/bin/node

// Check if there is a second command-line argument and store it in 'secondArg'
const secondArg = process.argv[2];

// Check if there is a third command-line argument
if (process.argv[3]) {
  console.log('Arguments found');
} 
// If there's no third argument but a second argument exists
else if (secondArg) {
  console.log('Argument found');
} 
// If no second or third argument is present
else {
  console.log('No argument');
}


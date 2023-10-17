#!/usr/bin/node
// script that prints My number if the first
// argument can be converted to an integer

if (isNaN(process.argv[2])) {
  console.log('Not a Number');
} else {
  console.log('My Number: ' + parseInt(process.argv[2]));
}

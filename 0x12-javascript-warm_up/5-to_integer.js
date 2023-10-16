#!/usr/bin/node
// script that prints My number if the first
//argument can be converted to an integer

if (NaN(process.argv[3])) {
	console.log('Not a Number');
} else {
	console.log('My Number: ' + parseInt(process.argv[3]));
}
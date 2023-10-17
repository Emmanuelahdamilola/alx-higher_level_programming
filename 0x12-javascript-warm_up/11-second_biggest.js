#!/usr/bin/node
// script that searches the second biggest
// integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const secondLargest = process.argv.slice(2).sort((a, b) => b - a)[1];
  console.log(secondLargest);
}

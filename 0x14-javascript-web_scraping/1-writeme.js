#!/usr/bin/node
// Importing the 'fs' module for file system operations
const fs = require('fs');

// Retrieving the file path and data to write from command-line arguments
const filePath = process.argv[2];
const writeData = process.argv[3];

// Writing data to the file asynchronously
fs.writeFile(filePath, writeData, 'utf-8', (error) => {
  // Handling errors, if any
  if (error) {
    console.log(error); // Log the error to the console
  }
});

#!/usr/bin/node
// Importing the 'fs' module for file system operations
const fs = require('fs');

// Retrieving the file path from the command-line arguments
const filePath = process.argv[2];

// Reading the file asynchronously
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.log(error); // Log the error to the console
  } else {
    console.log(data); // Log the file content to the console if successful
  }
});

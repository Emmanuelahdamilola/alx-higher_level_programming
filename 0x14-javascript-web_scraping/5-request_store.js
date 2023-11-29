#!/usr/bin/node
// Importing the 'request' module for making HTTP requests
const request = require('request');

// Importing the 'fs' module for file system operations
const fs = require('fs');

// Retrieving the URL and file path from command-line arguments
const url = process.argv[2];
const fileStream = fs.createWriteStream(process.argv[3]);

// Making an HTTP GET request to the specified URL and piping the response to a file stream
request
  .get(url)
  .pipe(fileStream);

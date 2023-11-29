#!/usr/bin/node
// Importing the 'request' module for making HTTP requests
const request = require('request');

// Retrieving the URL from command-line arguments
const url = process.argv[2];

// Making an HTTP GET request to the specified URL
request
  .get(url)
  .on('response', (response) => {
    // Handling the response event
    console.log('code: ' + response.statusCode); // Logging the HTTP status code to the console
  });

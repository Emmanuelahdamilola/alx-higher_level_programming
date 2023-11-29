#!/usr/bin/node
// Importing the 'request' module for making HTTP requests
const request = require('request');

// Retrieving the URL from command-line arguments
const url = process.argv[2];

// Making an HTTP GET request to the specified URL
request(url, (error, response, body) => {
  // Handling errors, if any
  if (error) {
    console.log(error); // Log the error to the console
  }

  // Parsing the JSON body of the response
  const jsonBody = JSON.parse(body);

  // Initializing a counter for characters related to Wedge Antilles
  let wedgeCount = 0;

  // Looping through each result in the API response
  for (const result of jsonBody.results) {
    // Looping through each character URL in the result
    for (const charURL of result.characters) {
      // Checking if the character URL includes the ID 18 (Wedge Antilles)
      if (charURL.includes(18)) {
        wedgeCount++; // Incrementing the counter if Wedge Antilles is found
      }
    }
  }

  // Logging the count of Wedge Antilles characters to the console
  console.log(wedgeCount);
});

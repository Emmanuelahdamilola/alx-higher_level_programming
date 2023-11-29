#!/usr/bin/node
// Importing the 'request' module for making HTTP requests
const request = require('request');

// Retrieving the movie ID from command-line arguments
const movieID = process.argv[2];

// Constructing the URL for the Star Wars API based on the movie ID
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

// Making an HTTP GET request to the specified URL
request(url, (error, response, body) => {
  // Handling errors, if any
  if (error) {
    console.log(error); // Log the error to the console
  }

  // Parsing the JSON body of the response
  const jsonBody = JSON.parse(body);

  // Logging the title of the movie to the console
  console.log(jsonBody.title);
});

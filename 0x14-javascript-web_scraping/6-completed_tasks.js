#!/usr/bin/node
// Importing the 'request' module for making HTTP requests
const request = require('request');

// Retrieving the URL from command-line arguments
const url = process.argv[2];

// Making an HTTP GET request to the specified URL
request(url, (err, resp, body) => {
  // Handling errors, if any
  if (err) {
    console.log(err); // Log the error to the console
  }

  // Object to store the count of completed tasks per user
  const completed = {};

  // Parsing the JSON body of the response
  const jsonBody = JSON.parse(body);

  // Looping through each task in the API response
  for (const task of jsonBody) {
    // Checking if the task is marked as completed
    if (task.completed) {
      // Updating the count of completed tasks for each user
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }

  // Logging the count of completed tasks per user to the console
  console.log(completed);
});

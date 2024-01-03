#!/usr/bin/node

/* Import the 'request' module for making HTTP requests*/
const request = require('request');

/* Extract the URL from the command-line argument */
const url = process.argv[2];

/* Make an HTTP request to the specified URL*/
request(url, function (err, response) {
  if (err) {
    /* If an error occurs during the request, print the error*/
    console.log('Error:', err);
  } else {
    /* If the request is successful, print the HTTP status code*/
    console.log('HTTP Status Code:', response.statusCode);
  }
});

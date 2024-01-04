#!/usr/bin/node
/**
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */
const myArgs = process.argv.slice(2);
const request = require('request');
request
  .get(myArgs[0])
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  })
  .on('error', error => {
    console.log(error);
  });

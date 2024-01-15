#!/usr/bin/node
/**
 * script that writes a string to a file.
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */
const myArgs = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(myArgs[0], myArgs[1],
  {
    encoding: 'utf-8',
    flag: 'w'
  },
  (error) => {
    if (error) {
      console.log(error);
    }
  });

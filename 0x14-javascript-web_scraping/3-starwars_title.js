#!/usr/bin/node
/**
 * a script that prints the title of a Star Wars movie where
 * the episode number matches a given integer
 * The first argument is the movie ID
 */
const myArgs = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${myArgs[0]}`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});

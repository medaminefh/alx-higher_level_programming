#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    for (const character of JSON.parse(body).characters) {
      request(character, function (error, _, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

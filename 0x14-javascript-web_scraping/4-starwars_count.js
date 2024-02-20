#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    let count = 0;
    for (const film of json.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

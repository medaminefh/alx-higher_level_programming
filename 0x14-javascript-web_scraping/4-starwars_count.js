#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const pattern = /\/people\/18\//g;
    const matches = body.match(pattern);
    console.log(matches.length);
  }
});

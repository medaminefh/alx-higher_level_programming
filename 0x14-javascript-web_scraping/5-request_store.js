#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

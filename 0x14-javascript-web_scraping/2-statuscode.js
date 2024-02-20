#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, _) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});

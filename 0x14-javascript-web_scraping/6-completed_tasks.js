#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = {};
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (obj[task.userId]) {
          obj[task.userId]++;
        } else {
          obj[task.userId] = 1;
        }
      }
    }
    console.log(obj);
  }
});

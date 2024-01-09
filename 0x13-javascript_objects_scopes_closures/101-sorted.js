#!/usr/bin/node
const { dict } = require('./101-data');

const obj = {};
const values = Object.values(dict);
for (const elem of values) {
  obj[elem] = [];
}

const entries = Object.entries(dict);
for (const elem of entries) {
  obj[elem[1]].push(elem[0]);
}
console.log(obj);

#!/usr/bin/node
const { list } = require('./100-data');

console.log(list);
const newArr = list.map((elem, index) => elem * index);
console.log(newArr);

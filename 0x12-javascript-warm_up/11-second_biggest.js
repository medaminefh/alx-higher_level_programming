#!/usr/bin/node
const argv = process.argv.slice(2);

function sortArr (arr) {
  if (arr.length < 2) {
    return '0';
  } else {
    return arr.map(Number).sort((a, b) => b - a)[1];
  }
}

const result = sortArr(argv);
console.log(result);

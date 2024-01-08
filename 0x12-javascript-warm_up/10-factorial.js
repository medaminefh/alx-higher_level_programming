#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const result = factorial(num);
console.log(result);

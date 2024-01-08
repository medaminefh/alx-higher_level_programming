#!/usr/bin/node
const argv = process.argv;
const converted = parseInt(argv[2]);
if (!converted) {
  console.log('Not a number');
} else {
  console.log('My number:', converted);
}

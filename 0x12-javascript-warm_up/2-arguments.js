#!/usr/bin/node
const argv = process.argv.length;
if (argv > 3) {
  console.log('Arguments found');
} else if (argv === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

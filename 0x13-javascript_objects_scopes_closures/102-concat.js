#!/usr/bin/node
const fs = require('fs');

const listFiles = process.argv.slice(2);
const d1 = fs.readFileSync(listFiles[0], 'utf-8');
const d2 = fs.readFileSync(listFiles[1], 'utf-8');
fs.writeFileSync(listFiles[2], d1 + d2);

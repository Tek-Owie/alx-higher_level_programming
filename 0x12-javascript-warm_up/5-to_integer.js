#!/usr/bin/node

const process = require('process');

const processArg = process.argv[2];

if (!parseInt(processArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(processArg)}`);
}

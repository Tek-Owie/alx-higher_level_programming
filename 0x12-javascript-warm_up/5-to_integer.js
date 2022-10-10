#!/usr/bin/node

const process = require('process');

const processArg = process.argv;

if (!parseInt(processArg[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt(processArg[2]));
}

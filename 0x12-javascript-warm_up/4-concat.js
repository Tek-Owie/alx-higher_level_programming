#!/usr/bin/node

const process = require('process');

const processArg = process.argv;

const argLength = processArg.length;

if (argLength < 3) {
  console.log('undefined is undefined');
} else if (argLength === 3) {
  console.log(`${processArg[2]} is undefined`);
} else {
  console.log(`${processArg[2]} is ${processArg[3]}`);
}

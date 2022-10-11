#!/usr/bin/node

const process = require('process');

const argLength = process.argv.length;

if (argLength > 3) {
  console.log('Arguments found');
} else if (argLength === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

#!/usr/bin/node

const process = require('process');

const processArg = process.argv;

if (!processArg[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

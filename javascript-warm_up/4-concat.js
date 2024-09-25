#!/usr/bin/node

const { argv } = require('node:process').slice(2);

console.log(argv[0] + ' is ' + argv[1]);

#!/usr/bin/node
const myVar = process.argv;
console.log((myVar[2] !== undefined) ? myVar[2] : 'No argument');

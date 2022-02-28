#!/usr/bin/node
const myVar = process.argv.slice(2);
switch (myVar.length) {
case 0:
    console.log('No argument');
    break;
case 1:
    console.log('Argument found');
    break;
default:
    console.log('Arguments found');
    break;
}

#!/usr/bin/node
const myVar = process.argv;
if (parseInt(myVar[2])) {
    const value = parseInt(myVar[2]);
    for (let i = 0; i < value; i++) {
	console.log('X'.repeat(value));
    }
} else {
    console.log('Missing size');
}

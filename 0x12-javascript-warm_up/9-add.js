#!/usr/bin/node
const myVar = process.argv;
function add (a, b) {
    return parseInt(a) + parseInt(b);
}
console.log(add(myVar[2], myVar[3]));

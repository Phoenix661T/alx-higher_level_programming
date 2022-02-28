#!/usr/bin/node
const myVar = process.argv;
function fac (num) {
    if (num !== 1) {
	return fac(num - 1) * num;
    }
    return 1;
}
if (myVar[2] !== undefined) {
    console.log(fac(parseInt(myVar[2])));
} else {
    console.log('1');
}

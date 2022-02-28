#!/usr/bin/node
let myVar = process.argv;
if (myVar[2] === undefined || myVar[3] === undefined) {
    console.log('0');
} else {
    myVar = myVar.slice(2).map(n => parseInt(n));
    let max = 0; let max2 = 0;
    for (let i = 0; i < myVar.length; i++) {
	if (myVar[i] >= max) {
	    max2 = max;
	    max = myVar[i];
	} else if (myVar[i] > max2) {
	    max2 = myVar[i];
}
}
console.log(max2);
}

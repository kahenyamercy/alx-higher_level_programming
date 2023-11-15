#!/usr/bin/node
const addNums = (a,b) => {
    return a + b;

}
console.log(addNums(Number(process.argv[2]), Number(process.argv[3])));

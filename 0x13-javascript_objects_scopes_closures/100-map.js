#!/usr/bin/node
const { list } = require('./100-data.js');

const myList = list.map((e, idx) => e * idx);
console.log(list);
console.log(myList);

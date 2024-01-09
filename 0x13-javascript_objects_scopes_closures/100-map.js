#!/usr/bin/node
const { list } = require('./100-date.js');
const myList = list.map((num, idx) => num * idx);
console.log(list);
console.log(myList);

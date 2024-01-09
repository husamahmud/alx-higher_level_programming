#!/usr/bin/node
const { list } = require('./100-data.js');

const l = list.map((el, i) => el * i);
console.log(list);
console.log(l);

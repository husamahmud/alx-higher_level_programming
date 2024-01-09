#!/usr/bin/node
const { dict } = require('./101-data.js');

const myDict = {};
Object.entries(dict).forEach(([key, value]) => {
  if (!myDict[value]) myDict[value] = [];
  myDict[value].push(key);
});

console.log(myDict);

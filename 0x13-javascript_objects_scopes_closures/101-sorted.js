#!/usr/bin/node
const { dict } = require('./101-data.js');

const myDict = {};
for (const userId in dict) {
  const cnt = dict[userId];
  if (myDict[cnt]) myDict[cnt].push(userId);
  else myDict[cnt] = [userId];
}

console.log(myDict);

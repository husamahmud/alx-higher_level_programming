#!/usr/bin/node
const num = process.argv[2];
if (!num || !Number.isInteger(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}

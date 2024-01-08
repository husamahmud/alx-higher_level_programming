#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  process.argv.sort((a, b) => b - a);
  console.log(process.argv[3]);
}

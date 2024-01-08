#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const maxNum = Number.max(process.argv);
  console.log(maxNum);
}

#!/usr/bin/node
function fact (n) {
  if (n === 0) return 1;
  return parseInt(n) * fact(parseInt(n) - 1);
}

console.log(fact(process.argv[2]));

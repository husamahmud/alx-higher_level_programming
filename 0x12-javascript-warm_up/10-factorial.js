#!/usr/bin/node
function fact (n) {
  if (n === 0) return 1;
  return parseInt(n) * fact(parseInt(n) - 1);
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(fact(process.argv[2]));
}

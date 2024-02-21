#!/usr/bin/node
const file = process.argv[1];
fetch(file)
  .then(res => res.text())
  .then(data => console.log(data))
  .catch(err => console.error(err));

#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], prcess.argv[3], (error) => {
  console.error(error);
});

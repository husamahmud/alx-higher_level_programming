#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res) => {
  if (err) console.error(err);
  console.log(`code: ${res.statusCode}`);
});

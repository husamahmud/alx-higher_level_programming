#!/usr/bin/node
const request = require('request');

const file = process.argv[1];
request({ url: file, encoding: 'UTF-8' }, (err, res, body) => {
  if (err) console.error(err);
  else if (res.statusCode !== 200) console.error(`Request failed. ${res.statusCode}`);
  else console.log(body);
});

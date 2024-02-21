#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) console.log(err);
  const data = JSON.parse(body);
  const chars = data.results.filter(f => f.characters.find(c => c.includes('18')));
  console.log(chars.length);
});

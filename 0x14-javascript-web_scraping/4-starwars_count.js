#!/usr/bin/node
const request = require('request');

const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;
request.get(process.argv[2], (err, res, body) => {
  if (err) console.error(err);
  const results = JSON.parse(body).results;
  for (let i = 0; i < results.length; i++) {
    if (results[i].characters.includes(wedgeAntilles)) count++;
  }
  console.log(count);
});

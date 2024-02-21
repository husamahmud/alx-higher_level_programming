#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  data.characters.map(ch => {
    request.get(ch, (err, res, body) => {
      if (err) {
        console.log(err);
      } else {
        const name = JSON.parse(body).name;
        console.log(name);
      }
    });
    return 0;
  });
});

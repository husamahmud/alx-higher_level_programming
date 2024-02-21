#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

function getCharacterNames (characters, index) {
  if (index < characters.length) {
    request.get(characters[index], (err, res, body) => {
      if (err) {
        console.log(err);
      } else {
        const name = JSON.parse(body).name;
        console.log(name);
        getCharacterNames(characters, index + 1);
      }
    });
  }
}

request.get(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    getCharacterNames(characters, 0);
  }
});

#!/usr/bin/node
const request = require('request');

const characterId = 18;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let wedgeAppearances = 0;

  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      wedgeAppearances++;
    }
  });

  console.log(wedgeAppearances);
});

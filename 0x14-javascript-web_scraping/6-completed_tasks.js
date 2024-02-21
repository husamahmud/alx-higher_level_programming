#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const obj = {};
    JSON.parse(body).map(todo => {
      if (todo.completed) obj[todo.userId] = (obj[todo.userId] || 0) + 1;
      return obj;
    });
    console.log(obj);
  }
});

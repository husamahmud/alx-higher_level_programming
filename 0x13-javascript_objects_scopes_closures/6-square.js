#!/usr/bin/node
const MySquare = require('./5-square');

class Square extends MySquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) console.log(c.repeat(this.height));
  }
}

module.exports = Square;

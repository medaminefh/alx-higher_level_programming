#!/usr/bin/node
const SquareM = require('./5-square');

class Square extends SquareM {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;

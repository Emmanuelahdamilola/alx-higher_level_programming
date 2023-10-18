#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let size = '';
      for (let j = 0; j < this.width; j++) {
        size = size + 'X';
      }
      console.log(size);
    }
  }
}

module.exports = Rectangle;

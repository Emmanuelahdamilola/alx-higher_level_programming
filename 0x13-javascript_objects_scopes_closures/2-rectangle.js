#!/usr/bin/node

// Define a class named 'Rectangle'
module.exports = class Rectangle {
  // Constructor function for the Rectangle class
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If the dimensions are invalid, create an instance of Rectangle
      Object.create(Rectangle);
    } else if (w && h) {
      // If valid dimensions are provided, set the width and height properties
      this.width = w;
      this.height = h;
    }
  }
};

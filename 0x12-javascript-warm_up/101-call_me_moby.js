#!/usr/bin/node

// function that executes x times a function.

exports.callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

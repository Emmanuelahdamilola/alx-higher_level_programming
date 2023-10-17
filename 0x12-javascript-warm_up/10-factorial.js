#!/usr/bin/node
// script that computes and prints a factorial

function computeFactorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

console.log(computeFactorial(parseInt(process.argv[2])));

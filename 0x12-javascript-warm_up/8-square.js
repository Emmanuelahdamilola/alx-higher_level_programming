#!/usr/bin/node
//script that prints a square

if (isNaN(process.argv[2])) {
  console.log("Missing size");
} else {
  const size = parseInt(process.argv[2]);
  const squareX = "X".repeat(size);

  for (let i = 0; i < size; i++) {
    console.log(squareX);
  }
}
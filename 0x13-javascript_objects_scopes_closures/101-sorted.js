#!/usr/bin/node

const { dict } = require('./101-data');

const totalList = Object.entries(dict);
const uniqueValues = [...new Set(Object.values(dict))];
const newDict = {};

uniqueValues.forEach((value) => {
  const list = totalList
    .filter(([key, val]) => val === value)
    .map(([key]) => key);
  newDict[value] = list;
});

console.log(newDict);

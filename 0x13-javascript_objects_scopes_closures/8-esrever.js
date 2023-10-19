#!/usr/bin/node

exports.esrever = function (list) {
  const reserveList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reserveList.push(list[i]);
  }
  return reserveList;
};

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      n++;
    }
  }
  return n;
};

#!/usr/bin/node

/* JavaScript
   Author: Ronald Aguirre
   Cuorse: JavaScript Warm up
*/

const number = process.argv[2];
const parseo = parseInt(number, 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseo}`);
}

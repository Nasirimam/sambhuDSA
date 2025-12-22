let a = 3,
  b = 4,
  c = 5;
let result = a > b ? (a > c ? a : c) : b > c ? b : c;
console.log(result);

let x = 12;
let y = x++ + ++x;
y++;
let z = ++y;
let p = x++ - ++y + z++;
console.log(x);
console.log(y);
console.log(z);
console.log(p);

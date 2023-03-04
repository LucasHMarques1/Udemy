// Trocar o valor das duas variáveis

let a = 7;
let b = 94;

a = a + b;
b = a - b;
a = a - b;

// depois da troca... a = 94 e b = 7
console.log("a = " + a);
console.log("b = " + b);


// OU


let A = 7;
let B = 94;
let AUX;

AUX = A;
A = B;
B = AUX;

// depois da troca... a = 94 e b = 7
console.log("A = " + A);
console.log("B = " + B);

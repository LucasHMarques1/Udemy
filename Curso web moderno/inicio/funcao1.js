// função sem retorno
function imprimirSoma(a, b) {
    console.log(a + b);
}

imprimirSoma(2, 3);
imprimirSoma(2); // NaN porque A = 2 e B = Undefined
imprimirSoma(2, 10, 4, 5, 6, 7, 8); // só pega os valores a função precisa, nesse caso os dois primeiros


// função com retorno
function soma(a, b = 0) {
    return a + b;
}

console.log(soma(2, 3)); // 5
console.log(soma(2)); // 2
console.log(soma()); // Nan

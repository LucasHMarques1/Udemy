console.log(soma(3, 4)) // funciona antes/depois do código

// function declaration
function soma(x, y) {
    return x + y
}

// function expression
const sub = function (x, y) {
    return x - y
}
console.log(sub(4, 2)) // só funciona depois do código

// named function expression
const mult = function mult(x, y) {
    return x * y
}
console.log(mult(3, 4)) // só funciona depois do código

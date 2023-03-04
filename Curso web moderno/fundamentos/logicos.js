// v e v -> v SÓ SE TODOS FOREM VERDADEIRO 
// v e f -> f
// f e ? -> f

// v ou ? ->  v
// f ou v -> f
// f ou f -> f

// v xor v -> f
// f xor f -> f
// v xor f -> v
// f xor v -> v

// !v -> f
// !f -> v

function compras(trabalho1, trabalho2) {
    const comprarSorvete = trabalho1 || trabalho2
    const comprarTv50 = trabalho1 && trabalho2
    // const comprarTv32 = !!(trabalho1 ^ trabalho2) // bitwise xor
    const comprarTv32 = trabalho1 != trabalho2
    const manterSaudavel = !comprarSorvete

    return { comprarSorvete, comprarTv50, comprarTv32, manterSaudavel}
    // MESMA COISA QUE 
    /* return { 
        comprarSorvete: comprarSorvete, 
        comprarTv50: comprarTv50, 
        comprarTv32: comprarTv32, 
        manterSaudavel: manterSaudavel
    } */
}

console.log(compras(true, true));
console.log(compras(true, false));
console.log(compras(false, true));
console.log(compras(false, false));

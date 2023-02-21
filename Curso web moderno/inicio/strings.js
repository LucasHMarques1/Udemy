const escola = "Cod3r";

console.log(escola.charAt(4)); // r
console.log(escola.charAt(5)) // vazio
console.log(escola.charCodeAt(3)); // néumero do digito "3" na tabela ASCII = 51
console.log(escola.indexOf('3'));

console.log(escola.substring(1)); // od3r
console.log(escola.substring(0 , 3)); // Cod

console.log('Escola '.concat(escola.concat("!")));
console.log(escola.replace(3, 'e')); // Coder

console.log('Ana, Maria, Pedro'.split(',')); // Criar um array a partir da ","

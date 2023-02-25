const funcs = [];

for(let j = 0; j < 10; j++){
    funcs.push(function(){
        console.log(j);
    })
}

funcs[2]() // 2
funcs[8]() // 8

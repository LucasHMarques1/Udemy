package condicional_ternario;

public class Main {
	
	public static void main (String[] args) {
		double preco = 34.5;
		double desconto;
		
		if(preco < 20.0) {
			desconto = preco * 0.1;
		} else {
			desconto = preco * 0.05;
		}
		System.out.println(desconto);
		
		// OU
		double precos = 34.5;
		double descontos = (preco < 20.0)? preco * 0.01: preco * 0.05;
		System.out.println(descontos);
	}

}

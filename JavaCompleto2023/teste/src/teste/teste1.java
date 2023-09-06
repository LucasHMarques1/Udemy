package teste;

import java.util.Locale;

public class teste1 {

	public static void main(String[] args) {
		
		System.out.println("Olá mundo!");
		System.out.println("Chegueeeei!");
		
		System.out.print("Olá mundo!");
		System.out.print("Chegueeeei!");
		
		int y = 32;
		System.out.println(" ");
		System.out.println("Número: " + y);
		
		double x = 10.35784;
		System.out.println("X = " + x);
		System.out.printf("%.2f%n", x);
		Locale.setDefault(Locale.US);
		System.out.printf("%.4f%n", x);
		
		System.out.printf("RESULTADO = %.2f METROS%n", x);
		char sexo = 'M';
		String nome = "Lucas";
		int idade = 19;
		System.out.printf("Meu nome é %s tenho %d do sexo %s e tenho R$ %.2f", nome, idade, sexo, x);

	}

}

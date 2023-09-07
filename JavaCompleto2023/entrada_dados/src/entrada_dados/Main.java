package entrada_dados;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// Ler pelo teclado
		String x;
		x = sc.next();
		System.out.println("Você digitou: " + x);
		
		// Ler inteiro
		int y;
		y = sc.nextInt();
		System.out.println("Você digitou: " + y);
		
		// Ler numero flutuante
		double z;
		z = sc.nextDouble();
		System.out.println("Você digitou: " + z);
		
		// Ler 1 caractere
		char a;
		a = sc.next().charAt(0);
		System.out.println("Você digitou: " + a);
		
		sc.close();	
	}

}

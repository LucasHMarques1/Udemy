package exercicio2;

import java.util.Scanner;

// Fazer um programa para ler um número inteiro, e depois dizer se este número é negativo ou não.

public class Program {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int num = sc.nextInt();
		if (num < 0) {
			System.out.println("Número negativo");
		} else {
			System.out.println("Número positivo");
		}

		sc.close();
	}
}

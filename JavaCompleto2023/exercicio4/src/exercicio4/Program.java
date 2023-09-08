package exercicio4;

import java.util.Scanner;

// Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o
// X, se for o caso.

public class Program {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int num = sc.nextInt();

		for (int i = 1; i <= num; i++) {
			if (i % 2 == 1) {
				System.out.println("Número impar:" + i);
			}
		}

		sc.close();
	}
}

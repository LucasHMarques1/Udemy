package estrutura_condicional;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// teste
		int x = 5;

		System.out.println("Bom dia");

		if (x > 0) {
			System.out.println("Boa tarde");
		} else {
			System.out.println("Boa noite");
		}

		// horario
		int hora;
		System.out.println("Que horas são?");
		hora = sc.nextInt();

		if (hora < 12) {
			System.out.println("Bom dia");
		} else {
			if (hora < 18) {
				System.out.println("Boa tarde");
			} else {
				System.out.println("Boa noite");
			}
		}
		
		// OU
		
		//if (hora < 12) {
		//	System.out.println("Bom dia");
		//} else if (hora < 18) {
		//		System.out.println("Boa tarde");
		//	} else {
		//		System.out.println("Boa noite");
		//	}
		// }

		sc.close();
	}}

package application;

import java.util.Locale;
import java.util.Scanner;

import entities.Salario;

public class Program {
	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		Salario salario = new Salario();
		
		System.out.println("Calculo Salário: ");
		System.out.print("Nome: ");
		salario.nome = sc.nextLine();
		System.out.print("Salário bruto: ");
		salario.salarioBruto = sc.nextDouble();
		System.out.print("Taxa: ");
		salario.taxa = sc.nextDouble();
		
		System.out.println(salario);
		
		System.out.print("Porcentagem do aumento: ");
		double porcentagem = sc.nextDouble();
		salario.aumento(porcentagem);
		
		System.out.println(salario);
		
		sc.close();
	} 

}

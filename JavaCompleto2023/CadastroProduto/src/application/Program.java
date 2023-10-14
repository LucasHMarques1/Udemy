package application;

import java.util.Locale;
import java.util.Scanner;

import entity.Product;

public class Program {
	
	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		Product product = new Product();
		System.out.println("Cadastro de produto: ");
		System.out.print("Nome: ");
		product.name = sc.nextLine();
		System.out.print("Preço: ");
		product.price = sc.nextDouble();
		System.out.print("Quantidade: ");
		product.quantity = sc.nextInt();
		System.out.println(product); /* Retorna sobre o produto e valores */
		
		System.out.println("Add produto: ");
		System.out.print("Quantos você deseja adicionar? ");
		int quantity = sc.nextInt();
		product.addProduto(quantity);
		System.out.println(product); /* Retorna sobre o produto e valores */
		
		System.out.println("Remover produto: ");
		System.out.print("Quantos você deseja remover? ");
		int quantity1 = sc.nextInt();
		product.removerProduto(quantity1);
		System.out.println(product); /* Retorna sobre o produto e valores */
		
		sc.close();
	}
	
}

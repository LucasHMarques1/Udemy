package entity;

public class Product {
	public String name;
	public double price;
	public int quantity;
	
	public double valorTotal() {
		return price * quantity;
	}
	
	public void addProduto(int quantity) {
		this.quantity += quantity;
	}
	
	public void removerProduto(int quantity) {
		this.quantity -= quantity;
	}
	
	public void respostaFinal() {
		System.out.println("");
	}
	
	public String toString() {
		return "Nome: " +
				name +
				"| Preço: " +
				price +
				"| Quantidade: " +
				quantity +
				"| Soma quantidade x preço = " +
				valorTotal();
	}
}
	
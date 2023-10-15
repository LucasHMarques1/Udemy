package entities;

public class Salario {
	public String nome;
	public double salarioBruto;
	public double taxa;
	
	public double salarioLiquido() {
		return salarioBruto - taxa;
	}
	
	public String toString() {
		return "Nome: " +
				nome +
				"| Salário liquido: " +
				salarioLiquido();
	}
	
	public void aumento(double porcentagem) {
	    salarioBruto += salarioBruto * (porcentagem / 100);
	}
}
package switch_case;

public class Main {

	public static void main(String[] args) {
		int x = 1;

		if (x == 1) {
			System.out.println("Hoje é domingo!");
		} else if (x == 2) {
			System.out.println("Hoje é segunda!");
		} else if (x == 3) {
			System.out.println("Hoje é terça!");
		} else if (x == 4) {
			System.out.println("Hoje é quarta!");
		} else if (x == 5) {
			System.out.println("Hoje é quinta!");
		} else if (x == 6) {
			System.out.println("Hoje é sexta!");
		} else if (x == 7) {
			System.out.println("Hoje é sábado!");
		} else {
			System.out.println("Erro");
		}

		// OU (Switch-case)
		int y = 1;

		switch (y) {
		case 1:
			System.out.println("Hoje é domingo!");
			break;
		case 2:
			System.out.println("Hoje é segunda!");
			break;
		case 3:
			System.out.println("Hoje é terça!");
			break;
		case 4:
			System.out.println("Hoje é quarta!");
			break;
		case 5:
			System.out.println("Hoje é quinta!");
			break;
		case 6:
			System.out.println("Hoje é sexta!");
			break;
		case 7:
			System.out.println("Hoje é sábado!");
			break;
		default:
			System.out.println("Erro");
			break;
		}
	}
}

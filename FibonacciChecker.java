import java.util.Scanner;

public class FibonacciChecker {

    public static String fibonacciCheck(int num) {
        int a = 0, b = 1;
        while (b < num) {
            int temp = a;
            a = b;
            b = temp + b;
        }
        if (b == num) {
            return "O número " + num + " pertence à sequência de Fibonacci!";
        } else {
            return "O número " + num + " não pertence à sequência de Fibonacci.";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num;

        if (args.length > 0) {
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Erro: O argumento fornecido não é um número inteiro válido.");
                return;
            }
        } else { // Caso contrário, solicita ao usuário que insira o número
            System.out.print("Digite um número para verificar se pertence à sequência de Fibonacci: ");
            num = scanner.nextInt();
        }

        String resultado = fibonacciCheck(num);
        System.out.println(resultado);
    }
}
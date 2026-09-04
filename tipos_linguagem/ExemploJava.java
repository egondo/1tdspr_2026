import java.util.Scanner;

public class ExemploJava {

    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        int soma = 0;
        System.out.print("Digite valor: ");
        int valor = tec.nextInt();
        while (valor != 0) {
            soma = soma + valor;
            System.out.print("Digite valor: ");
            valor = tec.nextInt();
        }
        System.out.println("O valor total é " + soma);
    } 
}
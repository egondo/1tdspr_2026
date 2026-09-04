#include <stdio.h>

int main() {
    int valor, soma = 0;
    printf("Informe o número: ");
    scanf("%d", &valor);
    while (valor != 0) {
        soma = soma + valor;
        printf("Informe o número: ");
        scanf("%d", &valor);
    }
    printf("A soma dos numeros vale %d", soma);
}
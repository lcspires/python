#include <stdio.h>

int main(void) {
	int e, t, v; // declaração de Variáveis via Indentificadores

    scanf("%d", &e); // especificador de conversão %d
    scanf("%d", &t); // operador de endereço &
    v = (e / t); // instrução de atribuição
    printf("%d", v); // prompt

    return 0; // passa o valor 0 para o ambiente
}

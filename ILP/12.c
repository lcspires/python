#include <stdio.h>
    
int main() {
    int mes;
    scanf("%d", &mes);

    switch (mes) {
        case 1: return printf("Janeiro");
        case 2: return printf("Fevereiro");
        case 3: return printf("Março");
        case 4: return printf("Abril");
        case 5: return printf("Maio");
        case 6: return printf("Junho");
        case 7: return printf("Julho");
        case 8: return printf("Agosto");
        case 9: return printf("Setembro");
        case 10: return printf("Outubro");
        case 11: return printf("Novembro");
        case 12: return printf("Dezembro");
        default: return printf("Mês Inválido");
    }

    return 0;
}

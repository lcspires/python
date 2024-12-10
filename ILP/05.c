#include <stdio.h>

enum pontuacoes {
    GOL = 100,
    DEFESA_EPICA = 75,
    DEFESA_NORMAL = 50,
    CHUTE_GOL = 10,
    EXPLOSAO = 100
};

int main() {
    
    int X, Y, Z, H, L, total_pontos;
    
    scanf("%d %d %d %d %d", &X, &Y, &Z, &H, &L);
    total_pontos = (X * GOL) + (Y * DEFESA_EPICA) + (Z * DEFESA_NORMAL) + (H * CHUTE_GOL) + (L * EXPLOSAO);
    printf("%d", total_pontos);

    return 0;
}


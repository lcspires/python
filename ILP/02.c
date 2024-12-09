#include <stdio.h>

int main(void) {
    int d, p, e;
	
	// lê dois inteiros separados por espaço numa mesma linha
	scanf("%d %d", &d, &p);
    e = (d * p / (d + p + 1));
    printf("%d", e);

    return 0;
}

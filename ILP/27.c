#include <stdio.h>

int main(void) { //brute-force
    int num;

    while (1) {
        scanf("%d", &num);
        if (num == 42) break;
        printf("%d\n", num);
    }

    return 0;
}

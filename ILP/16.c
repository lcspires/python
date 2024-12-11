#include <stdio.h>

int main(void){ // Calculadora do IMC

	float massa; // em quilogramas
	float altura; // em metros
	float IMC; // massa / (altura * altura)
	
	scanf("%f %f", &massa, &altura);
	IMC = massa / (altura * altura);
	
	// Classificação do IMC
    if (IMC < 17) {
        printf("muito-abaixo-do-peso");
    } else if (IMC < 18.5) {
        printf("abaixo-do-peso");
    } else if (IMC < 25) {
        printf("peso-normal");
    } else if (IMC < 30) {
        printf("acima-do-peso");
    } else if (IMC < 35) {
        printf("obesidade-1");
    } else if (IMC < 40) {
        printf("obesidade-2\n");
    } else {
        printf("obesidade-3\n");
    }
    
	return 0;
}

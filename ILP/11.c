#include <stdio.h>

int main(void){
	
	int X, Y;
	
	scanf("%d %d", &X, &Y);
	
	if (X == Y){
		printf("Você acertou!");
	}
	
	if (X != Y)	printf("Você errou!");
	
	return 0;
}

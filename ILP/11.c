#include <stdio.h>

int main(void){
	
	int X, Y;
	
	scanf("%d %d", &X, &Y);
	
	if (X == Y){
		printf("Voc� acertou!");
	}
	
	if (X != Y)	printf("Voc� errou!");
	
	return 0;
}

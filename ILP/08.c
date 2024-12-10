#include <stdio.h>

int main(void){
	
	struct Ponto {
	    int x;
	    int y;
	} p; // Declarando p
	
	p.x = 10;
	p.y = 20;
	printf("Ponto (%d, %d)\n", p.x, p.y);
	
	return 0;
}

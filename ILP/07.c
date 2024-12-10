#include <stdio.h>

int main(void){
	
	struct Ponto {
	    int x;
	    int y;
	};
	
	struct Ponto p = {10, 20};  // Declarando p
	printf("Ponto (%d, %d)\n", p.x, p.y);
	
	return 0;
}

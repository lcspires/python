#include <stdio.h>

int main(void){
	
	typedef struct {
	    int x;
	    int y;
	} Ponto; // "Ponto" é o novo nome para o tipo "struct { int x; int y; }"

	Ponto p; // // Declarando p
	
	p.x = 10;
	p.y = 20;
	printf("Ponto (%d, %d)\n", p.x, p.y);
	
	return 0;
}

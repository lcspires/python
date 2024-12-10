#include <stdio.h>

int main(void){
	
	typedef union { // só aceita uma alocação por vez
	    int inteiro;
	    char caractere;
	} Dados;
	
	Dados d;
	d.inteiro = 10;
	printf("Inteiro: %d\n", d.inteiro);
	d.caractere = 'L';
    printf("Caractere: %c", d.caractere); // d.inteiro é desalocado
	
	return 0;
}

#include <stdio.h>

int main(void){
	
	typedef union { // s� aceita uma aloca��o por vez
	    int inteiro;
	    char caractere;
	} Dados;
	
	Dados d;
	d.inteiro = 10;
	printf("Inteiro: %d\n", d.inteiro);
	d.caractere = 'L';
    printf("Caractere: %c", d.caractere); // d.inteiro � desalocado
	
	return 0;
}

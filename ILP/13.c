#include <stdio.h>

int main(void){
	
	/* requisitos para um pudim perfeito */
	const int tempo = 1259; // segundos
	const int condensado = 4; // caixas
	const int ovos = 8; // unidades
	const int leite = 2; // litros
	const int acucar = 1; // xicaras
	
	/* entradas do que o usuário possui */
	int C, O, L, X;
	scanf("%d %d %d %d", &C, &O, &L, &X);
	
	/* quanto de pudim ele pode produzir */
	C = C / condensado;
	O = O / ovos;
	L = L / leite;
	
	/* tempo gasto para fazer o máximo possível*/
	int h, m, s;
	
	if (C != 0 && C < O && C < L && C < X){
		s = C * tempo;
	}
	if (O != 0 && O < C && O < L && O < X){
		s = O * tempo;
	}
	if (L != 0 && L < O && L < C && L < X){
		s = L * tempo;
	}
	if (X != 0 && X <= O && X <= L && X <= C){
		s = X * tempo;
	}	
	
	h = s / 3600;
	s = s - (h * 3600);
	m = s / 60;
	s = s - (m * 60);
	
	printf("%d h %d m %d s", h, m, s);		
	
	return 0;
}

#include <stdio.h>

int main(void){
	
	int L, P, L1, L2, L3, P1, P2, P3;
	
	scanf("%d %d", &L1, &P1);
	scanf("%d %d", &L2, &P2);
	scanf("%d %d", &L3, &P3);
	
	L = L1 + L2 + L3;
	P = P1 + P2 + P3;
	
	if (L != P){
		if (L > P) printf("Lucas");
		else printf("Pedro");
	}
	else printf("Empate");
	
	return 0;
}

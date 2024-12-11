#include <stdio.h>

int main(void){
	
	float salario, salariof;
	
	scanf("%f", &salario);
	
	if (salario <= 6000){
		if (salario <= 3000) (salariof = salario-(salario*0.15));
		else (salariof = salario - ((salario-3000)*0.20) - 450);
	}
	else (salariof = salario - ((salario-6000)*0.30) - 1050);
	
	printf("Imposto: R$ %.2f\n", salario - salariof);
	printf("Salário Líquido: R$ %.2f", salariof);
	
	return 0;
}

#include<stdio.h>
int main()
{
	 float principal, rate, time, simpleInterest;
	 
	 printf("ENter number of principal:");
	 scanf("%f",&principal);
	  printf("ENter number of rate:");
	 scanf("%f",&rate);
	  printf("ENter number of time:");
	 scanf("%f",&time);
	 
	 simpleInterest=principal*rate*time/100;
	 
	 printf("sipleInterest number:%.2f",simpleInterest);

}

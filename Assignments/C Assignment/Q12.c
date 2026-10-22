//12.Write a Program to check the given number is prime or not prime.
#include<stdio.h>
int main()
{
	int n,prime=0;
	
	printf("Enter number:");
	scanf("%d",&n);
	
	if(n%2==0)
	prime++;
	
	if(n=1)
	{
		printf("Number is prime:",prime);
	}
	else
	{
		printf("Number id not prime",prime);
	}
	return 0;
}

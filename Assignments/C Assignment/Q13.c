//13.Write a program to find the Max number from the given three number 
//using Nested If 
#include<stdio.h>
int main()
{
	int a,b,c;
	
	printf("Enter number A,B,C:");
	scanf("%d%d%d",&a,&b,&c);
	
	if(a>b && a>c)
	{
		printf("A is greatest number");
	}
	else if(b>a && b>c)
	{
		printf("B is greatest number:");
	}
	else
	{
		printf("c is greatest number:");
	}
	return 0;
}

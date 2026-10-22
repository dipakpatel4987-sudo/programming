//10.Write a Program to check the given number is Positive, Negative.
#include<stdio.h>
int main()
{
	int n;

	printf("Enter number:");
	scanf("%d",&n);
	
	if(n>0)
	{
		printf("Number is pisitive:%d\n",n);
		
	}
	else if(n<0)
	{
		printf("Number is negative:%d\n",n);
		
	}
	else
	{
		printf("Number is Zero:");
	}	
	return 0;
}

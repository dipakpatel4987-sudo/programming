//9.Write a Program to show swap of two No's without using third variable.
#include<stdio.h>
int main()
{
	int a,b;
	
	printf("Enter a and b value:");
	scanf("%d%d",&a,&b);
	
	a=a+b;
	b=a-b;
	a=a-b;
	
	printf("Number of A:%d and Number of B:%d",a,b);
}

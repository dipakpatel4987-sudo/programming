//WAP to swap two numbers without using third variable
#include<stdio.h>
int main()
{
	int a,b;
	printf("Enter the value of A:");
	scanf("%d",&a);
	
	printf("Enter the value of B:");
	scanf("%d",&b);
		printf("before number swapping A:%d , B:%d \n",a ,b);
	
	a=a+b;
	b=a-b;
	a=a-b;
	
	printf("After number swapping A:%d , B:%d ",a ,b);
}

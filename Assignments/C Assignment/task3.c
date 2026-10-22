//Write a C program that accepts two integers from the user and performs
//arithmetic, relational, and logical operations on them. Display the results

#include<stdio.h>
int main(){
	int a,b;
	printf("Enter A number:");
	scanf("%d",&a);
	
	printf("Enter B number:");
	scanf("%d",&b);
	
	printf("Addition %d\n",a+b);
	printf("Subtraction %d\n",a-b);
	printf("multiply %d\n",a*b);
	printf("division %d\n",a/b);
}

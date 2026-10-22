//Write a C program that calculates the factorial of a number using a function.
//Include function declaration, definition, and call.
#include<stdio.h>

	int factorial(int n);
	
	
	int main(){
		int n,result;
		printf("Enter number:");
		scanf("%d",&n);
		
		result=factorial(n);
		
		printf("Factorial = %d", result);
		return 0;
	}
	int factorial(int n){
		int i,fact=1;
		
		for(i=1;i<=n;i++){
			fact=fact*i;
		}
	
	return fact;
	}

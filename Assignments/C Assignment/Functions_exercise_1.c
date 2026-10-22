//LAB EXERCISE 1: Fibonacci Sequence

//? Write a C program that generates the Fibonacci sequence up to N terms using a recursive
//function.
//? Challenge: Modify the program to calculate the Nth Fibonacci number using both iterative
//and recursive methods. Compare their efficiency.

#include<stdio.h>
fibonacci(n){
	int i,j;
	int a=0,b=1,c;
		for(i=0;i<n;i++){
		for(i=i+1;i<n;i++){
			c=a;
			a=b;
			b=c;
		}
	}
	
	printf("Nth Fibonacci Number = %d",c);

}
int main(){
	int n;
	
	
	printf("Enter your number:");
	scanf("%d",&n);
	
	printf(fibonacci());
	

    return 0;
}

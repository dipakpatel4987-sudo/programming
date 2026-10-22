//3. Loops
//LAB EXERCISE 1: Prime Number Check
//? Write a C program that checks whether a given number is a prime number or not using a for
//loop.
//? Challenge: Modify the program to print all prime numbers between 1 and a given number.
#include <stdio.h>

int main(){
	int n,i,j,prime;
	
	printf("Enter your limit:");
	scanf("%d",&n);
	
	printf("prime number between 1 to %d is\n",n);
	
	for(i=2;i<=n;i++)
	{
		prime=0;
		
		for(j=2;j<i;j++){
			if(i%j==0){
				prime=1;
				break;
			}
		}
	
	if(prime==0){
		printf("%d ",i);
	}
}
return 0;
}

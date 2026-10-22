//3. Loops
//LAB EXERCISE 2: Multiplication Table
//? Write a C program that takes an integer input from the user and prints its multiplication
//table using a for loop.
//? Challenge: Allow the user to in#include <stdio.h>
#include<stdio.h>
int main(){
	int num,range,i;
	
	printf("Enter table number:");
	scanf("%d",&num);
	printf("Enter table range :");
	scanf("%d",&range);
	
	for(i=1;i<=range;i++){
		printf("%d X %d = %d\n",num,i,num*i);
	}
	return 0;
}

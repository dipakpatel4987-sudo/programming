//1. Operators

//LAB EXERCISE 2: Check Number Properties

//? Write a C program that takes an integer from the user and checks the following using
//different operators:
//o Whether the number is even or odd.
//o Whether the number is positive, negative, orzero.
//o Whether the number is a multiple of both 3 and 5

#include <stdio.h>
int main()
{
	int num;
	
	printf("Enter an integer: ");
	scanf("%d",&num);
	
	if(num%2==0){
		printf("%d is even!!\n",num);
	}
	else
	printf("%d is odd!!\n",num);
	
	
	
	if(num>0){
		printf("%d is positive number!!\n",num);
	}
	else if(num<0)
	{
		printf("%d is negative!!\n",num);
	}
	else
	printf("%d is zero number!!\n",num);
	
	if(num%3==0 && num%5==0){
	printf("%d is a multiple of both 3 and 5.\n", num);}
    else
    	printf("%d is NOT a multiple of both 3 and 5.\n", num);
	
	return 0;
	
}

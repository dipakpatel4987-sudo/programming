//Write a C program to demonstrate pointer usage. Use a pointer to modify the
//value of a variable and print the result.

#include<stdio.h>
int main(){
	int num;
	printf("Enter number:");
	scanf("%d",&num);
	int *ptr;
	
	ptr=&num;
	
	printf("Befor modification:\n");
	printf("VAlue of number:%d\n",num);
	
	printf("\nChange number:");
	scanf("%d",&*ptr);
	
	printf("\nAfter modification:\n");
	printf("Value of number:%d",num);
}

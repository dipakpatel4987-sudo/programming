//LAB EXERCISE 3: Sum of Array Elements
//? Write a C program that takes N numbers from the user and stores them in an array. The
//program should then calculate and display the sum of all array elements.
//? Challenge: Modify the program to also find the average of the numbers.

#include<stdio.h>
int main(){
	
	int i,n;
	int arr[10];
	int sum=0;
	
	printf("Enter your number:");
	scanf("%d",&n);
	
	printf("Enter %d numbers:\n", n);
	
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++){
		sum+=arr[i];
	}
	printf("Sum of array elements = %d\n", sum);
	return 0;
}



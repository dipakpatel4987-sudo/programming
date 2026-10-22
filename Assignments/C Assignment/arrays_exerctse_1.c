//4. Arrays
//LAB EXERCISE 1: Maximum and Minimum in Array
//? Write a C program that accepts 10 integers from the user and stores them in an array. The
//program should then find and print the maximum and minimum values in the array.
//? Challenge: Extend the program to sort the array in ascending order.

#include<stdio.h>
int main(){
	int i,j,max,min,temp;
	int arr[10];
	
for(i=0;i<10;i++){
	printf("Enter your %d integer number:",i+1);
	scanf("%d",&arr[i]);
}
	
	max=min=arr[0];
	
	for(i=1;i<10;i++){
		
	
			if(arr[i]>max){
				max=arr[i];
			}
			if(arr[i]<min){
				min=arr[i];
			}
		
	}
	printf("max number:%d\n",max);
	printf("min number:%d",min);
	for(i=0;i<9;i++){
		for(j=i+1;i<10;j++){
		if (arr[i] > arr[j]){
		temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
	}
	}
	}
	printf("\n\nArray in Ascending Order:\n");
    for(i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;

	
}

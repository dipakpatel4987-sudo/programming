//LAB EXERCISE 2: Matrix Addition
//? Write a C program that accepts two 2x2 matrices from the user and adds them. Display the
//resultant matrix.
//? Challenge: Extend the program to work with 3x3 matrices and matrix multiplication.

#include<stdio.h>
int main(){
	int i,j;
	int a[2][2],b[2][2],sum[2][2];
	
	printf("Enter A input values:");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			scanf("%d",&a[i][j]);
		}
	}
	printf("Enter B input values:");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			scanf("%d",&b[i][j]);
		}
	}
	
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			sum[i][j]=a[i][j]+b[i][j];
		}
	}
	printf("\nResultant Matrix:\n");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("%d ",sum[i][j]);
		}
		printf("\n");
	}
	return 0;
}

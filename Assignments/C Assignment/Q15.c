//WAP to make simple calculator (operation include Addition, Subtraction,
//Multiplication, Division, modulo) 

#include<stdio.h>
int main()
{
	int num1,num2,choice;
	
	printf("Simple caluculator:\n");
	printf("<--------------->\n");
	
	printf("Enter value number 1:");
	scanf("%d",&num1);
	
	printf("Enter the value number 2:");
	scanf("%d",&num2);
	
	printf("<---mainu--->\n");
	printf("1.Addition :\n");
	printf("2.Subtraction :\n");
	printf("3.Multiplication :\n");
	printf("4.Division:\n");
	printf("5.Modulo :\n");
	
	printf("Enter the choice:");
	scanf("%d",&choice);
	
	switch(choice){
		case 1:
			printf("total Additon number %d",num1+num2);
			break;
	
		case 2:
			printf("total Subtraction number %d",num1-num2);
			break;
		
		case 3:
			printf("total Multiplication number %d",num1*num2);
			break;
		
		case 4:
			printf("total division number %d",num1/num2);
			break;
		case 5:
			if(num2 !=0){
				printf("Result %d",num1%num2);
			}
			else{
				printf("Modulo by zero not allowed!");
			}
			break;	
	default:
	printf("invalid number:");
	break;	
}
}

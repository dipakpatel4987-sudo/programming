//8.Write a program to calculate sum of 5 subjects & find the percentage. 
//Subject marks entered by user.
#include<stdio.h>
int main()
{
	int java,c,html,python,math,total;
	float totalper;
	
	printf("Enter java number:\n");
	scanf("%d",&java);
	
	printf("Enter C number:\n");
	scanf("%d",&c);
	
	printf("Enter HTML number:\n");
	scanf("%d",&html);
	
	printf("Enter python number:\n");
	scanf("%d",&python);
	
	printf("Enter math number:\n");
	scanf("%d",&math);
	
	total=java+c+html+python+math;
	
	printf("Total marks of all subject:%d\n",total);
	
	totalper=(total*100)/500;
	
	printf("Total percentage:%.2f",totalper);
	
}

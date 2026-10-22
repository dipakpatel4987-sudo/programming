//4.Write a program to find the Area of Circle 
#include<stdio.h>
int main()
{
	float redius,area;
	const float PI=3.14;
	
	printf("ENter the redius of circle:");
	scanf("%f",&redius);
	
	area=PI*redius*redius;
	
	printf("Area of circle=%2f\n",area);
	
	return 0;
}

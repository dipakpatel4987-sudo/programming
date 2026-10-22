//5.Write a program to find the Area of Triangle 
#include<stdio.h>
int main()
{
	float base, height, area;
	
	printf("ENter base:\n");
	scanf("%f",&base);
	
	printf("ENter height:\n");
	scanf("%f",&height);
	
	area=0.5*base*height;
	
	printf("area of triangle:%.2f",area);
}

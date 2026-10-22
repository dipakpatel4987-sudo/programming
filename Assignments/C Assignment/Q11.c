//11.Write a Program to check the given year is leap year or not. 
#include<stdio.h>
int main()
{
	int years;
	
	printf("Enter years:");
	scanf("%d",&years);
	
	if((years%4==0 && years %100!=0)||(years%400==0))
	{
		printf("%d years is leap years:",years);
	}
	else
	{
		printf("%d years is not leap years:",years);
	}
}

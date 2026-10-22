//7.Write a program to convert temperature from degree centigrade to 
//Fahrenheit.
#include<stdio.h>
int main()
{
	float celsius, fahrenheit;
	
	printf("Enter celsius:");
	scanf("%f",&celsius);
	
    fahrenheit = (celsius * 9 / 5) + 32;
    
    printf("fahrenheit number:%.2f",fahrenheit);

}

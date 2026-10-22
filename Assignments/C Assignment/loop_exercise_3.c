//3. Loops
//LAB EXERCISE 3: Sum of Digits
//? Write a C program that takes an integer from the user and calculates the sum of its digits
//using a while loop.
//? Challenge: Extend the program to reverse the digits of the number.
#include <stdio.h>

int main()
{
    int num, digit, reverse = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0)
    {
        digit = num % 10;
        reverse = reverse * 10 + digit;
        num = num / 10;
    }

    printf("Reversed number = %d", reverse);

    return 0;
}

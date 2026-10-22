//EXTRA LAB EXERCISES FOR IMPROVING PROGRAMMING LOGIC
// 1. Operators
//
// LAB EXERCISE 1: Simple Calculator
//
// ? Write a C program that acts as a simple calculator. The program should take two numbers
//and an operator as input from the user and perform the respective operation (addition,
//subtraction, multiplication, division, or modulus) using operators.
// ? Challenge: Extend the program to handle invalid operator inputs.


#include <stdio.h>

int main() {
    int num1, num2;
    char op;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    printf("Enter operator (+, -, *, /, %%): ");
    scanf(" %c", &op);

    switch(op) {
        case '+':
            printf("Result = %d\n", num1 + num2);
            break;

        case '-':
            printf("Result = %d\n", num1 - num2);
            break;

        case '*':
            printf("Result = %d\n", num1 * num2);
            break;

        case '/':
            if(num2 != 0)
                printf("Result = %d\n", num1 / num2);
            else
                printf("Division by zero is not allowed.\n");
            break;

        case '%':
            if(num2 != 0)
                printf("Result = %d\n", num1 % num2);
            else
                printf("Modulus by zero is not allowed.\n");
            break;

        default:
            printf("Invalid operator entered.\n");
    }

    return 0;
}

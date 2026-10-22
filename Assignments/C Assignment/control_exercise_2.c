//LAB EXERCISE 2: Number Comparison
//
//? Write a C program that takes three numbers from the user and determines:
//o The largest number.
//o The smallest number.
//? Challenge: Solve the problem using both if-else and switch-case statements.
#include <stdio.h>

int main() {
    int a, b, c;
    int largest, smallest;
    int choice;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    printf("\n1. Find Largest Number");
    printf("\n2. Find Smallest Number");
    printf("\nEnter your choice: ");
    scanf("%d", &choice);

    switch(choice) {

        case 1:
            if (a >= b && a >= c)
                largest = a;
            else if (b >= a && b >= c)
                largest = b;
            else
                largest = c;

            printf("Largest number = %d\n", largest);
            break;

        case 2:
            if (a <= b && a <= c)
                smallest = a;
            else if (b <= a && b <= c)
                smallest = b;
            else
                smallest = c;

            printf("Smallest number = %d\n", smallest);
            break;

        default:
            printf("Invalid choice!\n");
    }

    return 0;
}

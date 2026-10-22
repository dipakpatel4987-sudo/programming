//LAB EXERCISE 2: Factorial Calculation
//? Write a C program that calculates the factorial of a given number using a function.
//? Challenge: Implement both an iterative and a recursive version of the factorial function and
//compare their performance for large numbers.

#include <stdio.h>

long long fact_recursive(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * fact_recursive(n - 1);
}


long long fact_iterative(int n) {
    long long fact = 1;
    int i;

    for (i = 1; i <= n; i++) {
        fact *= i;
    }

    return fact;
}

int main() {
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    printf("\nRecursive Factorial of %d = %lld\n", n, fact_recursive(n));
    printf("Iterative Factorial of %d = %lld\n", n, fact_iterative(n));

    return 0;
}

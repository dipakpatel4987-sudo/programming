//Write a C program to create a file, write a string into it, close the file, then
//open the file again to read and display its contents.
#include <stdio.h>

int main() {
    FILE *fp;
    char data[] = "Hello! This is a file handling program in C.";
    char ch;

    fp = fopen("sample.txt", "w");

    if (fp == NULL) {
        printf("File could not be created.\n");
        return 1;
    }

    fprintf(fp, "%s", data);

    fclose(fp);

  
    fp = fopen("sample.txt", "r");

    if (fp == NULL) {
        printf("File could not be opened.\n");
        return 1;
    }

    printf("File Contents:\n");

    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);

    return 0;
}

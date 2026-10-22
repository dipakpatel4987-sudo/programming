//Write a C program that defines a structure to store a student's details (name,
//roll number, and marks). Use an array of structures to store details of 3
//students and print them.
#include<stdio.h>
struct student{
	char name[50];
	int roll;
	float marks;
};
int main(){
	struct student s[3];
	int i;
	
	for(i=0;i<3;i++){
		printf("\nEnter details of student %d:\n", i + 1);
		
		printf("Enter name:");
		scanf("%s",&s[i].name);
		printf("Enter roll no.:");
		scanf("%d",&s[i].roll);
		printf("Enter marks:");
		scanf("%f",&s[i].marks);
		
	}
	 printf("\n--- Student Details ---\n");
	 for(i=0;i<3;i++){
	 	printf("\nStudent %d:\n", i + 1);
	 	printf("Name: %s\n", s[i].name);
        printf("Roll Number: %d\n", s[i].roll);
        printf("Marks: %f\n", s[i].marks);
	 }
	 return 0;
}

#include<stdio.h>
int main()
{
	char a[50];
	int i,len;
	
	printf("Enter name:");
	gets(a);
	len=gets(a);
	for(i=0;i<len-1;i++){
		printf("%c",len);
	}
}

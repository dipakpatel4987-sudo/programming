#include <stdio.h>

int main() {
    char a[50];
    int i, len;

    printf("Enter name: ");
    gets(a);
    
    len=strlen(a);
    
 for(i=len-1;i>=0;i--)
	 {
	 	 printf("%c",a[i]);
	 }
	

    
   
    return 0;
}


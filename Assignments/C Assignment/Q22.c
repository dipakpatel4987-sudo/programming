#include<stdio.h>
int main(){
	int n,a=0,b=1,i,c;
	printf("Enter the number:");
	scanf("%d",&n);
	printf("A number is %d",a);
	printf("B number is %d",b);
	for(i=3;i<=n;i++){
		c=a+b;
		printf("%d\n",c);
		a=b;
		b=c;
	
	}
}

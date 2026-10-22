#include<stdio.h>
int main(){
	int n,i,rev=0;
	printf("ENter the number for reverse:");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++){
		rev=rev*10+(n%10);
		n=n/10;
	}
	printf("reverse number:%d",rev);
}

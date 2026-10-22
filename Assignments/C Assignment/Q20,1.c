// WAP to take 10 no. Input from user and find out …
#include<stdio.h>
int main()
{
	int n ,i,sum=0,ev=0,odd=0,totalev=0,totalodd=0;
	
	
	for(i=1;i<=10;i++){
		printf("Enter the number:");
	    scanf("%d",&n);
		sum=sum+n;
		if(n%2==0){
			totalev=totalev+n;
			ev++;
		}
		else{
			totalodd=totalodd+n;
			odd++;
		}
	}
	printf("total sum is: %d\n",sum);
	printf("total ev number is :%d\n",ev);
    printf("total odd number is :%d\n",odd);
	printf("total ev sum number is :%d\n",totalev);
	printf("total odd number sum is: %d\n",totalodd);
}

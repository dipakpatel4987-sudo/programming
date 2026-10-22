#include<stdio.h>
int main(){

int a[5],b[5],n1,n2,i,j,temp,ch;

printf("Enter the first array number:");
scanf("%d",&n1);
for(i=0;i<n1;i++){
	scanf("%d",&a[i]);
}
printf("Enter the second array number:");
scanf("%d",&n2);
for(i=0;i<n2;i++){
	scanf("%d",&b[i]);
}
	printf("\n1. Ascending Order\n");
    printf("2. Descending Order\n");
    printf("Enter your choice: ");
    scanf("%d",&ch);
    
    if(ch==1)
    {
    	for(i=0;i<5;i++){
    		for(j=i+1;j<n1;j++){
    			if(a[i]>a[j]){
    				temp=a[i];
    				a[i]=a[j];
    				a[j]=temp;
				}
			}
		}
			for(i=0;i<5;i++){
    		for(j=i+1;j<n2;j++){
    			if(b[i]>b[j]){
    				temp=b[i];
    				b[i]=b[j];
    				b[j]=temp;
				}
			}
		}
	}
	 else if(ch==2)
    {
    	for(i=0;i<5;i++){
    		for(j=i+1;j<n1;j++){
    			if(a[i]<a[j]){
    				temp=a[i];
    				a[i]=a[j];
    				a[j]=temp;
				}
			}
		}
			for(i=0;i<5;i++){
    		for(j=i+1;j<n2;j++){
    			if(b[i]<b[j]){
    				temp=b[i];
    				b[i]=b[j];
    				b[j]=temp;
				}
			}
		}
	}
printf("\nvalue of first array number \n");
for(i=0;i<5;i++){
	printf("%d",a[i]);
}
printf("\nvalue of sacond array number \n");
for(i=0;i<5;i++){
	printf("%d",b[i]);
}
}

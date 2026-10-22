//14.Write a program to find the Max number from the given three number 
//using Ternary Operator 
int main()
{
	int a,b,c,max;
	
	printf("Enter number A,B,C:");
	scanf("%d%d%d",&a,&b,&c);
	
	 max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
	 
	 printf("max number:%d",max);
}

#include<iostream>
using namespace std;

int main(){
	int row;
	int i,j;
	
	cout<<"Enter row:";
	cin>>row;
	
	cout << "\nRight-Angled Triangle:\n";
	
	for(i=1;i<=row;i++){
		for(j=1;j<=i;j++)
		{
			cout<<"*";
		}
		cout<<endl;
	}
	return 0;
}

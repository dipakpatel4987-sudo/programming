#include<iostream>
using namespace std;

int main(){
	int num,i;
	
	cout<< "Enter a number: ";
    cin >> num;
    cout << "Multiplication table "<<num<<endl;
    
    for(i=1;i<=10;i++){
    	cout<<num<<"x"<<i<<"="<<num*i<<endl;
    	
	}
	return 0;


}

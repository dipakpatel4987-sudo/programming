#include<iostream>
using namespace std;

int main(){
	int num1=10;
	float result1;
	 result1=num1;
	 
	 int num2=10.75;
	 float result2;
	
	result2=(int)num2;
	
	cout<<"Implicit Type Conversion:"<<endl;
	cout<<"Intger value"<<num1<<endl;
	cout<<"converted into float"<<result1<<endl;
	
	
	cout << "\nExplicit Type Conversion:" << endl;
    cout << "Float value = " << num2 << endl;
    cout << "Converted to Integer = " << result2 << endl;
    
    return 0;

}

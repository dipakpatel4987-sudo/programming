#include<iostream>
using namespace std;

int main(){
	int age=20;
	float salary=50000.90;
	char grade='A';
	string name="Dipak";
	
	const float pi=3.14159;
	
	cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Salary: " << salary << endl;
    cout << "Grade: " << grade << endl;
    cout << "PI: " << pi << endl;
    
    age=age+5;
    salary=salary+5000;
    
    cout << "\nAfter Operations:" << endl;
    cout << "Updated Age: " << age << endl;
    cout << "Updated Salary: " << salary << endl;
    return 0;
}

#include<iostream>
using namespace std;

int main(){
	float marks;
	
	cout<<"Enter your marks :";
	cin >> marks ;
	
	if (marks < 0 || marks > 100){
		cout<<"Invalid marks! Please enter marks between 0 and 100.";
	}
	else if(marks>=90){
		cout << "Grade: A+";
    }
    else if (marks >= 80) {
        cout << "Grade: A";
    }
    else if (marks >= 70) {
        cout << "Grade: B";
    }
    else if (marks >= 60) {
        cout << "Grade: C";
    }
    else if (marks >= 50) {
        cout << "Grade: D";
    }
    else {
        cout << "Grade: F (Fail)";
    }

    return 0;

	
}

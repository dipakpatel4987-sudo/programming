//Basic Input/Output 
//o Write a C++ program that accepts user input for their name and age and then 
//displays a personalized greeting. 
//o Objective: Practice input/output operations using cin and cout. 

#include<iostream>
using namespace std;

int main(){
	string name;
	int age;
	
	cout<<"Enter Your Name:";
	getline(cin,name);
	
	cout<<"Entre Your Age:";
	cin>>age;
	
	cout<<"\n Name:"<<name<<"You are "<<age<<"Years old"<<endl;
}

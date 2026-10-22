//POP vs. OOP Comparison Program 
//o Write two small programs: one using Procedural Programming (POP) to calculate the 
//area of a rectangle, and another using Object-Oriented Programming (OOP) with a 
//class and object for the same task. 
//o Objective: Highlight the difference between POP and OOP approaches.

#include<iostream>
using namespace std;
//Procedural Programming (POP) Approach
//int main()
//{
//	float area,length,width;
//	
//	cout<<"Enter the length of rectangle:";
//	cin>>length;
//	
//	cout<<"Enter the wedth of ractangle:";
//	cin>>width;
//	
//	area=length*width;
//	
//	cout<<"Total area of the ractangle:"<<area<<endl;
//}
//Object-Oriented Programming (OOP) Approach

class Rectangle{
	private:
		float length,width;

public:
	void getdata(){
		cout<<"Enter the length of rectangle:";
		cin>>length;
	
		cout<<"Enter the wedth of ractangle:";
		cin>>width;
	}
	float calculateArea()
	{
		return length*width;
	}
};
int main(){
	Rectangle rect;
	rect.getdata();
	
	cout<<"Area of rectangle:"
	<<rect.calculeteArea()<<endl;
}

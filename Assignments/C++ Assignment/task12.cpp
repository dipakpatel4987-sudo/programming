#include<iostream>
using namespace std;

float add(float a,float b){
	return a+b;
}
float subtract(float a,float b){
	return a-b;
}
float multiply(float a,float b){
	return a*b;
}
float divide(float a,float b){
	 if (b == 0) {
        cout << "Error! Division by zero is not allowed." << endl;
        return 0;
    }
    return a / b;

}

int main(){
	float num1, num2;
    char choice;

    cout << "===== Simple Calculator =====" << endl;
    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    cout << "\nChoose an operation:" << endl;
    cout << "+ : Addition" << endl;
    cout << "- : Subtraction" << endl;
    cout << "* : Multiplication" << endl;
    cout << "/ : Division" << endl;
    cout << "Enter your choice: ";
    cin >> choice;
 switch (choice) {
        case '+':
            cout << "Result = " << add(num1, num2) << endl;
            break;

        case '-':
            cout << "Result = " << subtract(num1, num2) << endl;
            break;

        case '*':
            cout << "Result = " << multiply(num1, num2) << endl;
            break;

        case '/':
            cout << "Result = " << divide(num1, num2) << endl;
            break;

        default:
            cout << "Invalid operation!" << endl;
    }

    return 0;
}

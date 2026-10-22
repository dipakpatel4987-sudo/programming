#include <iostream>
using namespace std;


int num = 100;


void displayLocal() {
    int num = 50;   
    cout << "Local variable inside function = " << num << endl;
}


void displayGlobal() {
    cout << "Global variable inside function = " << ::num << endl;
}

int main() {
    cout << "Global variable in main = " << num << endl;

    displayLocal();
    displayGlobal();

    return 0;
}

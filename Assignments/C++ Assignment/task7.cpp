#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 5;

    
    cout << "===== Arithmetic Operators =====" << endl;
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    cout << "a / b = " << a / b << endl;
    cout << "a % b = " << a % b << endl;

   
    cout << "\n===== Relational Operators =====" << endl;
    cout << "a == b : " << (a == b) << endl;
    cout << "a != b : " << (a != b) << endl;
    cout << "a > b  : " << (a > b) << endl;
    cout << "a < b  : " << (a < b) << endl;
    cout << "a >= b : " << (a >= b) << endl;
    cout << "a <= b : " << (a <= b) << endl;

   
    cout << "\n===== Logical Operators =====" << endl;
    cout << "(a > 5 && b > 2) : " << ((a > 5) && (b > 2)) << endl;
    cout << "(a > 5 || b > 10): " << ((a > 5) || (b > 10)) << endl;
    cout << "!(a > b)         : " << !(a > b) << endl;

   
    cout << "\n===== Bitwise Operators =====" << endl;
    cout << "a & b = " << (a & b) << endl;
    cout << "a | b = " << (a | b) << endl;
    cout << "a ^ b = " << (a ^ b) << endl;
    cout << "~a = " << (~a) << endl;
    cout << "a << 1 = " << (a << 1) << endl;
    cout << "a >> 1 = " << (a >> 1) << endl;

    return 0;
}

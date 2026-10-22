#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance;  

public: 
    BankAccount() {
        balance = 0;
    }

   
    void deposit(double amount) {
        balance += amount;
        cout << "Deposited: " << amount << endl;
    }

    
    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: " << amount << endl;
        } else {
            cout << "Insufficient Balance!" << endl;
        }
    }

    
    void displayBalance() {
        cout << "Current Balance: " << balance << endl;
    }
};

int main() {
    BankAccount account;

    account.deposit(5000);
    account.withdraw(2000);
    account.displayBalance();

    return 0;
}

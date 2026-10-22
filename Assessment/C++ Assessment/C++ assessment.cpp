#include <iostream>
#include <ctime>
using namespace std;

class ATM
{
private:
    int pin;
    double balance;

public:
    
    ATM();

    void welcomeScreen();
    void helpScreen();
    bool login();
    void menu();
    void deposit();
    void withdraw();
    void checkBalance();
};


ATM::ATM()
{
    pin = 12345;
    balance = 60000;
}


void ATM::welcomeScreen()
{
    time_t now = time(0);

    cout << "\n=====================================\n";
    cout << "      WELCOME TO ATM BANKING\n";
    cout << "=====================================\n";
    cout << "Current Date & Time : " << ctime(&now);

    cout << "\n1. Login\n";
    cout << "2. Help\n";
    cout << "3. Exit\n";
}


void ATM::helpScreen()
{
    cout << "\n========== HELP ==========\n";
    cout << "1. Insert ATM Card\n";
    cout << "2. Enter ATM PIN (12345)\n";
    cout << "3. Select Transaction\n";
    cout << "4. Deposit Money\n";
    cout << "5. Withdraw Money\n";
    cout << "6. Check Balance\n";
    cout << "7. Exit\n";
}


bool ATM::login()
{
    int enteredPin;

    cout << "\nEnter ATM PIN : ";
    cin >> enteredPin;

    if (enteredPin == pin)
    {
        cout << "\nPIN Verified Successfully.\n";
        return true;
    }
    else
    {
        cout << "\nIncorrect PIN.";
        cout << "\nOnly One Attempt Allowed.";
        cout << "\nExiting...\n";
        return false;
    }
}


void ATM::deposit()
{
    double amount;

    cout << "\nCurrent Balance : Rs. " << balance;
    cout << "\nEnter Deposit Amount : ";
    cin >> amount;

    balance += amount;

    cout << "\nDeposit Successful.";
    cout << "\nUpdated Balance : Rs. " << balance << endl;
}


void ATM::withdraw()
{
    double amount;

    cout << "\nEnter Withdrawal Amount : ";
    cin >> amount;

    if (amount > balance)
    {
        cout << "\nInsufficient Balance!";
        cout << "\nTransaction Failed.\n";
    }
    else
    {
        balance -= amount;
        cout << "\nWithdrawal Successful.";
        cout << "\nRemaining Balance : Rs. " << balance << endl;
    }
}


void ATM::checkBalance()
{
    cout << "\nAvailable Balance : Rs. " << balance << endl;
}


void ATM::menu()
{
    int choice;

    do
    {
        cout << "\n========== ATM MENU ==========\n";
        cout << "1. Deposit\n";
        cout << "2. Withdraw\n";
        cout << "3. Check Balance\n";
        cout << "4. Exit\n";

        cout << "\nEnter Choice : ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            deposit();
            break;

        case 2:
            withdraw();
            break;

        case 3:
            checkBalance();
            break;

        case 4:
            cout << "\nThank You For Using ATM.\n";
            break;

        default:
            cout << "\nInvalid Choice.\n";
        }

    } while (choice != 4);
}

int main()
{
    ATM obj;

    int choice;

    do
    {
        obj.welcomeScreen();

        cout << "\nEnter Choice : ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            if (obj.login())
            {
                obj.menu();
            }
            break;

        case 2:
            obj.helpScreen();
            break;

        case 3:
            cout << "\nThank You!\n";
            break;

        default:
            cout << "\nInvalid Choice.\n";
        }

    } while (choice != 3);

    return 0;
}

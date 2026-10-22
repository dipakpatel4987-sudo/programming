#include<iostream>
using namespace std;

int main(){
	int sercetnumber=75;
	int guess;
	
	cout << "===== Number Guessing Game =====" << endl;
    cout << "Guess a number between 1 and 100." << endl;
    
    
	while (true){
		
		
		cout << "Enter your guess: ";
	    cin >> guess;
			
		if(guess< 0 || guess > 100){
			cout<<" Please enter a number between 1 and 100.";
		}
		else if(guess < sercetnumber){
			 cout<<"Too low! Try again." << endl;
		}
		else if(guess > sercetnumber){
			 cout<<"Too high! Try again." << endl;
		}
		else{
			 cout << "Congratulations! You guessed the correct number: "<<sercetnumber << endl;
	            	break;
	            }
	            
	}
return 0;	 
}

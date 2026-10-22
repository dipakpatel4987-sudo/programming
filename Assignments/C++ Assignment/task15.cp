#include<iostream>
using namespace std;

int main(){
	int n,i,sum=0;
	float avarege;
	
	cout << "Enter the number of elements: ";
    cin >> n;
    
    int arr[n];
    cout << "Enter " << n << " integers:" << endl;
    for(i=0;i < n;i++){
    	cin>>arr[i];
	}
	for(i=0;i<n;i++){
    	sum+=arr[i];
	}
	avarege=(float)sum / n;
	cout << "\nArray Elements: ";
	for(i=0;i<n;i++){
    	cout<<arr[i]<<" ";
	}
	cout << "\nSum = " << sum << endl;
    cout << "Avarege = " << avarege << endl;

    return 0;
}



#include <iostream>
using namespace std;

int main(){

	int times, a; 
	
	cin >> times;
	
	for (int x=0; x<times; x++)
	{
		cin >> a;
		if (a%2 == 1)
			cout << "1\n";
		else
			cout << "0\n";


	}
	return 0;
}

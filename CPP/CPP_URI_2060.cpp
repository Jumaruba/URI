/*
4 Multiplo(s) de 2
0 Multiplo(s) de 3
2 Multiplo(s) de 4
3 Multiplo(s) de 5
*/

#include <iostream>
using namespace std;

int main()
{
	int times, number;
	int _2=0, _3=0, _4=0, _5=0;

	cin >> times;

	for (int i=0; i < times; i++)
	{
		cin >> number;
	
	if (number %2 == 0)
		_2++;
	if (number %3 ==0)
		_3++;
	if (number %4 ==0)
		_4++;
	if (number %5 ==0)
		_5++;
	}

	cout << _2 <<" Multiplos(s) de 2\n";
	cout << _3 <<" Multiplos(s) de 3\n";
	cout << _4 <<" Multiplos(s) de 4\n";
	cout << _5 <<" Multiplos(s) de 5\n";

return 0;

} 



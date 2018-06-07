#include <iostream>
using namespace std; 

int main()
{
	int times, codigo;
	double quant, total;

	total = 0;
	cin >> times;

	for (int i=0; i<times; i++)
	{
		cin >> codigo>> quant;
		if (codigo == 1001)
			total +=(1.50*quant);
		else if (codigo == 1002)
			total+= (2.50*quant);
		else if (codigo == 1003)
			total+= (3.50*quant);
		else if (codigo == 1004)
			total+= (4.50*quant);
		else
			total+= (5.50*quant);
	}

	printf("%.2f\n", total);
	return 0;
}

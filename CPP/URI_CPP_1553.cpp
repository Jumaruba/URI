#include <iostream>
#include <vector>

using namespace std;

int main(){

	vector <int> xuliane_foda(1000);
	int pergunta, frequencia, numero, total = 0;
	cin >> pergunta >> frequencia; 

	while (pergunta!= 0 && frequencia!= 0){
		for (int i = 0; i < pergunta; i++){
			cin >> numero;
			xuliane_foda[numero-1]++;
		}
		for (int i = 0; i< pergunta; i++){
			if (xuliane_foda[i] >= frequencia){
				total++;
			}
			
		}
		cout << total << endl;
		total = 0;

		for (int i = 0; i< pergunta; i++){
			xuliane_foda[i] = 0;
		}

		cin >> pergunta >> frequencia;
	


	}


	return 0;
}

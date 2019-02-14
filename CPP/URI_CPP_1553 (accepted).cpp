#include <iostream>
#include <vector>

using namespace std;

int main(){

	vector <int> xuliane_foda(1000);
	int pergunta, frequencia, numero, total = 0;
	cin >> pergunta >> frequencia; 

	while (pergunta!= 0 && frequencia!= 0){  //pushing the frequency of each question
		for (int i = 0; i < pergunta; i++){
			cin >> numero;
			xuliane_foda[numero-1]++;
		}
		for (int i = 0; i< pergunta; i++){  //searching for elements which are greater than frequencia
			if (xuliane_foda[i] >= frequencia){
				total++;
			}
			
		}
		cout << total << endl;
		total = 0;

		for (int i = 0; i< pergunta; i++){  //cleaning the vector again
			xuliane_foda[i] = 0;
		}

		cin >> pergunta >> frequencia;
	


	}


	return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1553

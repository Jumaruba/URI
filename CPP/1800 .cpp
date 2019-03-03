#include <iostream>
#include<vector>

using namespace std;

int main(){
	vector <int> escritorios(1001,1);

	int semana, dias, escritorio;

	cin >> semana >> dias; 

	for (int i = 0; i < dias; i++){
		cin >> escritorio;
		escritorios[escritorio] = 0;
	}
	for (int i = 0; i< semana; i++){
		cin >> escritorio;
		if (escritorios[escritorio] == 1){
			cout << escritorios[escritorio] << endl;
			escritorios[escritorio] = 0;
		}

		else{
			cout << "0" << endl;
		}
	}
	return 0;
}


//https://www.urionlinejudge.com.br/judge/pt/problems/view/1800

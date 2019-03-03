#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> notas = {100,50,20,10,5,2,1};
    int numero;
    cin >> numero;
    cout <<  numero << endl;
    for (int i= 0; i < 7; i++){
        cout << numero/notas[i] << " nota(s) de R$ " << notas[i] <<",00" << endl;
        numero = numero%notas[i];

    }

    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

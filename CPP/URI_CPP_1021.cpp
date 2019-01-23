
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main()
{
    vector<int> notas = {100,50,20,10,5,2}, moedas = {100,50,25,10,5,1};
    double dinheiro;
    int inteiro, inteiro2;
    cin >> dinheiro;
    inteiro = int(dinheiro);
    cout << "NOTAS:" << endl;
    for (int i = 0; i<6; i++){
        cout << inteiro/notas[i] << " nota(s) de R$ " << notas[i] << ".00" << endl;
        inteiro = inteiro%notas[i];
    }
    
    cout << "MOEDAS:" << endl;
    inteiro2 = int(dinheiro);
    inteiro = (dinheiro - inteiro2 + inteiro)*100;
    cout << fixed << setprecision(2);
    for (int i= 0; i< 6; i++){
        dinheiro = moedas[i];
        dinheiro = dinheiro/100;
        cout << inteiro/moedas[i] << " moeda(s) de R$ " << dinheiro << endl;
        inteiro = inteiro%moedas[i];
    }

    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

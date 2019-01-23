
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double codigo, numero, preco, fim;
    cin >> codigo >> numero >> preco;
    fim  = numero*preco;
    cin >> codigo >> numero >> preco;
    fim = fim + numero*preco;
    
    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << fim << endl;
    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

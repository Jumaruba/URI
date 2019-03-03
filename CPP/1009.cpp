
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    string nome;
    double fixo, comissao;
    cin >> nome;
    cin >> fixo >> comissao;
    cout << fixed << setprecision(2);
    cout << "TOTAL = R$ " << fixo+comissao*0.15 << endl;

    return 0;
}


//https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

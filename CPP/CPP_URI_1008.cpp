#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double numero, horas, preco;
    cin >> numero >> horas >> preco;
    cout << "NUMBER = " << numero << endl;
    cout<< fixed << setprecision(2);
    cout << "SALARY = U$ " << horas*preco << endl;

    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

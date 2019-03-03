
#include <iostream>
#include <iomanip>    //setprecision
using namespace std;

int main()
{
    double pi = 3.14159, area, raio;
    cin >> raio;
    cout << fixed << setprecision(4);   //to limit decimals
    cout << "A=" << pi*raio*raio << endl;

    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

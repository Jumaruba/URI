#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int a, b, c, maior;
    cin >> a >> b >> c;
    maior = (a + b+ abs(a-b))/2;
    maior = (c + maior + abs(maior - c))/2;
    cout << maior << " eh o maior" << endl;

    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

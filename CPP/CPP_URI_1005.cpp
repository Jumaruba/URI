
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double a, b;
    cin >> a >> b;
    cout << fixed << setprecision (5);
    cout << "MEDIA = " << (3.5*a+b*7.5)/11 << endl;

    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

#include <iostream>
using namespace std;

int main()
{
    double a, b, c;

    cin >> a>> b>> c;

    if (a>=(b+c) || b>=(a+c) || c>=(a+b))

        cout << "NAO FORMA TRIANGULO\n";



    else if (a*a == (b*b + c*c) || b*b == (a*a + c*c) || c*c == (a*a + b*b))

        cout << "TRIANGULO RETANGULO\n";



    else if (a*a > (b*b + c*c) || b*b > (a*a + c*c) || c*c > (a*a + b*b))

        cout << "TRIANGULO OBTUSANGULO\n";



    else if(a*a < (b*b + c*c) || b*b < (c*c + a*a) || c*c < (a*a + b*b))

        cout << "TRIANGULO ACUTANGULO\n";



    if(a == b && c == b)
        cout << "TRIANGULO EQUILATERO\n";



    else if(a==b && a!=c || a==c && b!=a || c==b && c!=a)

        cout << "TRIANGULO ISOSCELES\n";



    return 0;

}
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int item, quantidade;
    float numero;
    cin >> item >> quantidade;
    cout << fixed << setprecision(2);
    if (item == 1){
        numero = quantidade;
        numero = 4*numero;
        cout << "Total: R$ " << numero<< endl;
    }
    else if (item == 2){
        numero = quantidade;
        numero = 4.5*numero;
        cout << "Total: R$ " << numero<< endl;
    }
    
    else if (item == 3){
        numero = quantidade;
        numero = 5*numero;
        cout << "Total: R$ " << numero<< endl;
    }
    else if (item == 4){
        numero = quantidade;
        numero = 2*numero;
        cout << "Total: R$ " << numero<< endl;
    }
    else if (item == 5){
        numero = quantidade;
        numero = 1.5*numero;
        cout << "Total: R$ " << numero<< endl;
    }
    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

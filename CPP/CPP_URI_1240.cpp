#include <iostream>
#include <math.h>
using namespace std;


int main()
{   
    int a, b, copy, n;
    int contador = 0;
    cin >> n ;  //how many cicles 
    
    for (int i = 0; i < n; i++){

    cin >> a >> b;
    copy = b;
    contador = 0;
    while (copy!= 0){   // how many numbers we have in b
        contador++;
        copy = copy/10;}

    contador = pow(10, contador);  // the final digits
    if (fmod(a, contador)!=b) { 
        cout << "nao encaixa" << endl;
    }
    else 
        cout << "encaixa" << endl;
    
    }
    return 0;
}

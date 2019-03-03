#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{   
    float in= 0; 
    int dias = 0;
    int numero;
    cin >> numero;
    for (int i=0; i< numero; i++){
        cin >> in;
        while (in> 1){
            in = in/2;
            dias ++;
        }
        cout << dias << " dias" << endl;
        dias = 0;
    }

    return 0;
}

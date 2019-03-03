#include <iostream>

using namespace std;

int main()
{
    float virgula;
    int contador;
    for (int i= 0; i<6; i++){
        cin >> virgula;
        if (virgula> 0)   
            contador ++;
            
    }
    cout << contador << " valores positivos" << endl;
    
    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

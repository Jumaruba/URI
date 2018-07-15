#include <iostream>
using namespace std;

int main(){
    string a, b;
    int times;
    cin >> times;
    for (int i=0; i<times; i++){
        cin >> a;
        cin >> b;
        if (a== "ataque" && b ==  "pedra"){
            cout << "Jogador 1 venceu" << endl;
        }
        if (b ==  "ataque" && a ==  "pedra"){
            cout << "Jogador 2 venceu" << endl;
        }
        if (a == "pedra" && b == "papel"){
            cout << "Jogador 1 venceu"<< endl;
        }
        if (b ==  "pedra" && a ==  "papel"){
            cout << "Jogador 2 venceu" << endl;
        }
        if (a ==  "ataque" && b ==  "papel"){
            cout << "Jogador 1 venceu" << endl;
        }
        if (b ==  "ataque" && a==  "papel"){
            cout << "Jogador 2 venceu" << endl;
        }
        if (a ==  "papel" && b ==  "papel"){
            cout << "Ambos venceram" << endl;
        }
        if (a ==  "pedra" && b ==  "pedra"){
            cout<< "Sem ganhador" << endl;
        }
        if (a ==  "ataque" && b ==  "ataque"){
            cout << "Aniquilacao mutua" << endl;
        }
    }
}
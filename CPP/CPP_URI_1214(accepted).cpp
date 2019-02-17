#include <iostream>
#include <iomanip>
#include <vector> 
using namespace std; 

int main(){
    int casos, alunos, nota, soma = 0, media, contador;
    float fim;
    vector <int> n; 
    cout << fixed << setprecision(3);
    cin >> casos;
    for (int i = 0; i < casos; i++){
        cin >> alunos;
        soma = 0;
        n.clear();
        for (int j = 0; j< alunos; j++) {  //finding out the media
            cin >> nota;
            n.push_back(nota);
            soma += nota;
        }
        media = soma/alunos;
        contador = 0;
        for (int j = 0; j < alunos; j++){   //couting how many students are above media
            if (n[j] > media)
                contador++;
        }
        fim = (float)contador*100/alunos;   //dont forget the (float)
        cout << fim << "%" << endl;
    }
    return 0;
}


//https://www.urionlinejudge.com.br/judge/pt/problems/view/1214

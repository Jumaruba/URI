#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main() {
    int quantidade;
    while(scanf("%d", &quantidade) != EOF){
        // we want to create a new vector organized
        
        vector <int> quero, tenho;
        int aux = 0, contador= 0;
        bool swapped = true;

        //ewe are inputing the first vector
        for (int i = 0; i < quantidade; i++){
            cin>> aux;
            quero.push_back(aux);
        }

        //we are inputing the second vector

        for (int i = 0; i< quantidade; i++){
            cin >> aux;
            tenho.push_back(aux);
        }

        //vwe are creating the new list

        vector <int> nova(quantidade);
        
        for (int i = 0; i < quantidade; i++){
            contador = 0;
            while (quero[i] != tenho[contador])
                contador++;
            nova[contador] = i;
        }

        //let's apply bubble sort algorithm
        contador = 0;  // this is to count how many swap we did
        while (swapped == true){
            swapped = false;
            for (int i = 1; i < quantidade; i++){
                if (nova[i-1]> nova[i]){
                    swap(nova[i],nova[i-1]);
                    swapped = true;
                    contador ++;

                }
            }
        }
        cout << contador << endl;
    }
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1228

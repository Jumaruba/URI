#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main() {
    int quantidade;
    while(scanf("%d", &quantidade) != EOF){
        //primeira parte serC! organizar a nova lista para poder aplicar o algoritmo de sort
        
        vector <int> quero, tenho;
        int aux = 0, contador= 0;
        bool swapped = true;

        cin >> quantidade; 

        //estamos criando o primeiro vetor
        for (int i = 0; i < quantidade; i++){
            cin>> aux;
            quero.push_back(aux);
        }

        //estamos criando o segundo vetor

        for (int i = 0; i< quantidade; i++){
            cin >> aux;
            tenho.push_back(aux);
        }

        //vamos criar a nova lista

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

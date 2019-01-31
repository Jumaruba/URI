#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;


int main(){
    string n;
    int soma = 0, b1, b2;
    //lets calculate the b1 digit

    while (cin >> n){
    string nova;
    soma = 0;
    b1 = 0;
    b2 = 0;
    for (int i = 0; i< n.size(); i++){ 
        soma += (n[i]%48)*(9-i);
    }
    
    soma = soma%11;
    if (soma == 10)
        soma = 0;

    b1 = soma;
    soma = 0;

    //lets calculate the b2 digit

    for (int i = 1; i < n.size()+1; i++){
        soma += (n[i-1]%48)*i;
    }
    soma = soma%11;
    if (soma == 10)
        soma = 0;

    b2 = soma;
    
    //lets put it in the right format

    for (int i = 0; i< n.size(); i++){
        nova.push_back(n[i]);
        if (i == 2 || i == 5)
            nova.push_back('.');
    } 

    nova.push_back('-');
    nova.push_back(b2+48);
    nova.push_back(b1+48);
    cout << nova << endl;
    }
    return 0;
}

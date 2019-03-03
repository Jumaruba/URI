#include <iostream>
#include <string>

using namespace std;

int main(){
    int quantidade;
    string palavra, nova = "";

    cin >> quantidade;
    cin.ignore();
    for (int j = 0; j< quantidade; j++) {

        getline(cin, palavra);

        for (int i = palavra.size() / 2 - 1; i > -1; i--) {  //geting the first half
            nova.push_back(palavra[i]);
        }

        for (int i = palavra.size() - 1; i >= palavra.size() / 2; i--)  //geting the second half
            nova.push_back(palavra[i]);


        for (int i = 0; i < nova.size(); i++)  //printint the result
            cout << nova[i];
        cout << endl;
        nova = "";
    }

    return 0;

}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

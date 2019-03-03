#include <iostream>
#include <string>
#include <vector>

using namespace std;

int maximo(int arg1,int arg2){ //getting the max between two numbers;
    if (arg1> arg2)
        return arg1;
    else
        return arg2;
}

string get_word(vector<string> palavras){  //getting the string to be analysed;

    int passos, x, y;
    string letras, resultado;


    cin >> passos >> x >> y;
    cin.clear();
    cin.ignore();
    getline(cin, letras);
    x--;
    y--;
    resultado.push_back(palavras[x][y]);

    for (int i = 0; i< passos ; i++){
        if (letras[i] == 'E'){
            resultado.push_back(palavras[x][y+1]);
            y+=1;
        }
        else if (letras[i] == 'W'){
            resultado.push_back(palavras[x][y-1]);
            y+=1;
        }
        else if (letras[i] == 'S'){
            resultado.push_back(palavras[x+1][y]);
            x+= 1;
        }
        else if (letras[i] == 'N'){
            resultado.push_back(palavras[x-1][y]);
            x-=1;
        }

    }
    return resultado;

}

int LCS(string s1, string s2, long s1_size, long s2_size){  //applying the longest common string algorithm;
    if (s1_size <= 0 || s2_size <= 0)
        return 0;
    if (s1[s1_size-1] == s2[s2_size-1])
        return 1 + LCS(s1, s2, s1_size - 1, s2_size - 1);
    else
        return maximo(LCS(s1, s2, s1_size -1, s2_size), LCS (s1, s2, s1_size, s2_size-1));
}


int main() {

    int casos, linhas, comprimento;
    string word, s1, s2;
    long result, s1_size, s2_size;

    cin >> casos;

    for (int i = 0; i < casos; i++) {  //a for loop for the cases
        vector<string> palavras;
        cin >> linhas >> comprimento;


        for (int j = 0; j < linhas; j++) { //creating matrix
            cin >> word;
            palavras.push_back(word);
        }

        s1 = get_word(palavras);
        s2 = get_word(palavras);
        s1_size = s1.size();
        s2_size = s2.size();
        result = LCS(s1, s2, s1_size, s2_size);
        cout << "Case " << i+1 << ": " << s1_size -result << " " << s2_size - result << endl;
    }
}

//https://www.urionlinejudge.com.br/judge/en/problems/view/1341
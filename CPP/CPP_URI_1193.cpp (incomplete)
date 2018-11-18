#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;


vector<int> hexa_vector = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
int hexdec(string hexa){
    int decimal = 0;
    for (int i= 0; i< hexa.length(); i++){
        for (int j=0; j< 16; j++){
            if (hexa[i]== hexa_vector[j]){
                decimal += pow(16,hexa.length()-i-1)*j;
            }
        } 
    }
    return decimal;
}

int bindec(string bin){
    int decimal = 0;
    for (int i= 0; i< bin.length(); i++){
        if (bin[i] == '1'){
            decimal+= pow(2,bin.length()-i-1);
        }
    }
    return decimal;
}

string decbin(int dec){
    string bin = "";
    bin += to_string(dec%2);

    while (dec/2!=0){
        dec = dec/2;
        bin += to_string(dec%2);
    }
    reverse(bin.begin(),bin.end());
    return bin;
}

string dechex (int dec){
    string valor = "";
    valor += hexa_vector[dec%16];

    while (dec/16!=0){
        dec = dec/16;
        valor += hexa_vector[dec%16];
        dec = dec/16;
    
    }
    reverse(valor.begin(),valor.end());
    return valor;
}

int main(){
    
    int times;
    string number;
    string form;
    cin >> times;
    for (int i=0; i< times; i ++){
        cin >> number >> form;
        cout << "Case " << i+1 << ":" << endl;
        if (form == "bin"){
            cout << bindec(number) << " dec"<< endl;
            cout << hexdec(to_string(bindec(number))) << " hex" << endl;
        }
        else if (form == "hex"){
            cout << hexdec(number) << " dec" << endl;
            cout << decbin(hexdec(number)) << " bin" << endl;
        }
        else if (form == "dec"){
            cout << dechex(stoi(number)) << " hex" << endl;
            cout << decbin(stoi(number)) << " bin" << endl;
        }
        cout << endl;
    }    
    return 0;
    
}

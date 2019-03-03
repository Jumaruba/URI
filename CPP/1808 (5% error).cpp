#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(){
    string media;
    float quero, contador, total;
    cin >> media;

    for (int i = 0; i < media.size() ; i++){
        if (media[i] != 49){
            total += media[i]%48;
       
        }
        else if (i != media.size()-1){
            if (media[i+1] == 48 && media[i] == 49){
                total += 10;
                i++;
              
            }
            else
                total++;
        
        }
        contador ++;
    }
    cout << fixed << setprecision(2);
    cout << total/contador << endl;
    return 0;
}

//I get 5% wrong, I dont know why
//https://www.urionlinejudge.com.br/judge/pt/problems/view/1808

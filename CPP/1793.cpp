#include <iostream>

using namespace std;

int main(){
    int pessoas, tempo, momento, k;
    cin >> pessoas;
    while (pessoas!=0){
        for (int i = 0; i< pessoas; i++){
            cin >> k;
            if (i == 0)
                momento = k;
                
            else {
                if (momento + 10 < k){
                    tempo += 10;
                    momento = k;
                }
                else{
                    tempo += k-momento;
                    momento = k;
                }

            }
        }
        tempo += 10;
        cout << tempo << endl;
        tempo = 0;
        cin >> pessoas;
    }
    return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1793

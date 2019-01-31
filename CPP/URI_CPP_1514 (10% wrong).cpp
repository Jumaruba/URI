#include <iostream>
#include <vector>

using namespace std;

int main(){
    int c1, c2, c3, c4, participantes, problemas, aux;
    bool rule1, rule4, rule2, rule3;
    // inputing matrix

    cin >> participantes >> problemas;
    while (participantes != 0 && problemas != 0){
    
        int matrix[participantes][problemas];
        c4 = 1;
        for (int i = 0; i< participantes; i++){
            rule1 = false;
            rule4 = false;
            for (int j = 0; j< problemas; j++){
                cin >> aux;
                matrix[i][j] = aux;
                if (aux == 0)
                    rule1 = true;
                if (aux == 1)
                    rule4 = true;
            }
            if (rule1 == true)
                c1 = 1;
            if (rule4  == false)
                c4 = 0;
        }
        c2 = 1;
        c3 = 1;
        for (int i = 0; i< participantes; i++){
            rule2 = false;
            rule3 = false;
            for (int j = 0; j< problemas; j++){
                if (matrix[j][i] == 1)
                    rule2 = true;
                if (matrix[j][i] == 0)
                    rule3 = true;
                }

        if (rule2 == false)
            c2 = 0;
        if (rule3 == false)
            c3 = 0;
        }
        cout << c1+c2+c3+c4 << endl;
        c1 = 0; c2 = 0; c3 = 0; c4 = 0;
     
    
        cin >> participantes >> problemas;}
    return 0;
}

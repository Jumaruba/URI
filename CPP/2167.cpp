#include <iostream>

using namespace std;

int main(){
    int n, rpm; 
    int anterior = 0; 
    bool there = false;
    cin >> n; 

    for (int i = 0; i< n; i++){
        cin >> rpm;
        if (rpm >= anterior){
            anterior = rpm;
        }
        else {
            cout << i+1 << endl;
            there = true;
            break;
        }
    }

    if (!there)
        cout << 0 << endl; 

    return 0;
}
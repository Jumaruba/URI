#include <iostream>
#include <string>
using namespace std;

int main() {
    string l;
    int size;
    cin >> l;
    size = l.size();
    for (int i = size-1; i>=0; i--){
        cout<< l[i];
    }
    cout << endl;

    return 0;
}
#include <iostream>

using namespace std;

int main(){
	int jogadores, partidas, gols, total = 0;
	bool todas = true;
	cin >> jogadores >> partidas;

	for (int i = 0; i < jogadores; i++){
		todas = true;   //let's suppose that the player did points
		for (int j = 0; j < partidas; j++){
			cin >> gols;
			if (gols == 0)  //if the didn't do any points in a game, than todas = false
				todas = false;
		}
		if (todas == true)
			total ++;
	}

	cout << total << endl;
	return 0;
}

//https://www.urionlinejudge.com.br/judge/pt/problems/view/1715

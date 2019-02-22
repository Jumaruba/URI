# C++
Here are some problems from https://www.urionlinejudge.com.br/judge/pt in c++.


## Some instructions

Here a few intructions that I've used in some problems, that maybe important for you.

#### 1. How to change floating point precision

```
 #include <iomanip>

   cout << fixed << setprecision(x);
```
  
_In x you put how you want to format and from that line on, all the floating points will appear in that format._


#### 2. Bubble Sort  (https://visualgo.net/pt/sorting)

```
while (swapped == true){
    swapped = false;
    for (int i = 1; i < n; i++){
        if (nova[i-1]> nova[i]){
            swap(nova[i],nova[i-1]);
            swapped = true;
                    
                
 ```
 
 #### 3. How many numbers
 
```
int algarismos(int n){  
    int contador = 1;

    while (n/10 != 0){
        n = n/10;
        contador ++;
    }
	return contador;
 ```
 
 #### 4. Dont't forget
 
 If you wanna use cin.getline(word) after cin >> word1, you need to put cin.ignore() after cin >> word1.
 
 For more exercises check https://codingcompetitions.withgoogle.com/ 

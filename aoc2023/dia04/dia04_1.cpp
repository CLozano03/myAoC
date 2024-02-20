/**
 * Compilar: g++ -o dia04_1 dia04_1.cpp
 * Ejecutar: ./dia04_1 < input.txt
 */

#include <iostream>
#include <sstream>
#include <queue>
#include <cmath>

using namespace std;

int read_card(){
    int n_winning_cards = 0;


    string linea;
    string token = "";
    
    priority_queue<int> monticulo1, monticulo2;
    int m1_top, m2_top;

    getline(cin, linea);
    istringstream iss(linea);

    iss >> token; iss >> token; // Salta "Card" y "n:"
    iss >> token;

    while(token != "|"){
        monticulo1.push(stoi(token));
        iss >> token;
    }
       
    while(iss >> token){
        monticulo2.push(stoi(token));
    }

    // Monticulos ordenados de mayor a menor
    while(!monticulo1.empty() && !monticulo2.empty()){
        m1_top = monticulo1.top();
        m2_top = monticulo2.top();

        if(m1_top == m2_top){
            monticulo1.pop(); monticulo2.pop();
            n_winning_cards++;
        } else if (m1_top > m2_top){
            monticulo1.pop();
        } else {
            monticulo2.pop();
        }
            
    }
    
    //Calcula el valor de 'worth_points' en base a la cantidad de cartas ganadoras
    return n_winning_cards == 0 ? 0 : pow(2, n_winning_cards - 1); 
}

int main(){
    int suma_wp = 0;
    while(!cin.eof()){
        suma_wp += read_card();
    }
    cout << "Suma \"worth_points\": " << suma_wp << endl;

    return 0;
}
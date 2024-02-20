/**
 * Compilar: g++ -o dia04_2 dia04_2.cpp
 * Ejecutar: ./dia04_2 < input.txt
 */

#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

#define N_CARDS 198

int n_winning_cards(priority_queue<int> m1, priority_queue<int> m2){
    int n_winning_cards = 0;
    int m1_top, m2_top;

     // Monticulos ordenados de mayor a menor
    while(!m1.empty() && !m2.empty()){
        m1_top = m1.top();
        m2_top = m2.top();

        if(m1_top == m2_top){
            m1.pop(); m2.pop();
            n_winning_cards++;
        } else if (m1_top > m2_top){
            m1.pop();
        } else {
            m2.pop();
        }
    }

    return n_winning_cards;
}

int suma_arr(vector<int> arr){
    int suma = 0;
    for(int i = 0; i < (int)arr.size(); i++){
        suma += arr[i];
    }
    return suma;
}


int read_cards(){
    int n_carta = 0;
    int cartas_ganadoras;

    std::priority_queue<int> monticulo1, monticulo2;
    std::vector<int> scratchcards(N_CARDS, 1);

    string linea;
    string token = "";
    

    while(getline(cin, linea)){
        istringstream iss(linea);

        iss >> token; iss >> token; // Salta "Card" y "n:"
        iss >> token;
        
        while(token != "|"){ monticulo1.push(stoi(token)); iss >> token; }
        while(iss >> token){ monticulo2.push(stoi(token)); }

        cartas_ganadoras = n_winning_cards(monticulo1, monticulo2);

        for(int i = 1; i <= cartas_ganadoras; i++){
            scratchcards[n_carta + i] += scratchcards[n_carta];
        }
        
        // Limpiar monticulos
        while(!monticulo1.empty()){ monticulo1.pop(); }
        while(!monticulo2.empty()){ monticulo2.pop(); }

        n_carta++;
    }
 
    return suma_arr(scratchcards); 
}

int main(){
    cout << "Total \"scratchcards\": " << read_cards() << endl;
    return 0;
}
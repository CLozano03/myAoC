/**
 * Compilar: g++ dia07_1.cpp  handRanker_1.cpp -o dia07_1 -g
 * Ejecutar: ./dia07_1 < input.txt
 */

#include <iostream>
#include <sstream>
#include <queue>

#include "handRanker.hpp" // Incluye handRanker

using namespace std;

priority_queue<pair<string, int>, vector<pair<string, int>>, handRanker> orderedHands;

void read_file(){
    string linea;
    while(getline(cin,linea)){
        istringstream iss(linea);
        string hand;
        int bid;
        iss >> hand;
        iss >> bid;
        orderedHands.push(make_pair(hand, bid));
    }
} 

long suma_winning_points(){
    long suma_wp = 0;
    int rank = 1;
    while(!orderedHands.empty()){
        pair<string, int> top = orderedHands.top(); orderedHands.pop();
        suma_wp += top.second * rank;
        rank++;
    }
    return suma_wp;
}

int main(){
    int res;
    
    read_file(); 

    res = suma_winning_points();
    cout << "Total winnings: " << res << endl;

    return 0;
}
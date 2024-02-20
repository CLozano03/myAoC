/**
 * Compilar: g++ -o dia06_2 dia06_2.cpp
 * Ejecutar: ./dia06_2 < input.txt
 */

#include <iostream>
#include <sstream>
#include <utility> // std::pair

using namespace std;

/* Devuelve un par <tiempo, distancia> */
pair<long,long> read_file(){
    pair<long, long> res;
    long tiempo = 0 , distancia = 0;
    string linea1, linea2;
    getline(cin, linea1); getline(cin, linea2);

    for(char c : linea1){
        if(isdigit(c))
            tiempo = tiempo * 10 + (c - '0');
    }

    for(char c : linea2){
        if(isdigit(c))
            distancia = distancia * 10 + (c - '0');
    }   

    res = make_pair(tiempo, distancia);
    return res;
}

bool beats_record(long tiempo_total, long tiempo, long distancia){
    return tiempo * (tiempo_total - tiempo) > distancia;
}

int ways_to_beat(long tiempo, long distancia){
    int contador = 0;

    for (int i = 0; i < tiempo; i++){
        if(beats_record(tiempo, i, distancia))
            contador++;
    }
    return contador;    
}


int main(){
    int res;

    pair<long, long> input = read_file();

    res = ways_to_beat(input.first, input.second);
    cout << "Ways to beat: " << res << endl;

    return 0;
}
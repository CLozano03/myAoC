/**
 * Compilar: g++ -o dia06_1 dia06_1.cpp
 * Ejecutar: ./dia06_1 < input.txt
 */

#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define N_RACES 4

std::vector<int> tiempos(N_RACES, 0);
std::vector<int> distancias(N_RACES, 0);

void read_file(){
    string token;
    string linea1, linea2;
    getline(cin, linea1); getline(cin, linea2);

    istringstream is1(linea1);
    istringstream is2(linea2);

    is1 >> token; is2 >> token; // Salta "Time" y "Distance"
    
    for(int i = 0; i < N_RACES; i++){
        is1 >> tiempos[i];
        is2 >> distancias[i];
    }
}

bool beats_record(int tiempo_total, int tiempo, int distancia){
    return tiempo * (tiempo_total - tiempo) > distancia;
}

int ways_to_beat(int n_carrera){
    int contador = 0;
    int tiempo = tiempos[n_carrera];
    int distancia = distancias[n_carrera];

    for (int i = 0; i < tiempo; i++){
        if(beats_record(tiempo, i, distancia)){
            contador++;
        }
    }
    return contador;    
}


int main(){
    int res = 1;
    read_file();

    for(int i = 0; i < N_RACES; i++){
        res *= ways_to_beat(i);
    }  

    cout << "Multiplicacion: " << res << endl;

    return 0;
}
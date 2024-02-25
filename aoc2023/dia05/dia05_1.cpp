/**
 * Compilar: g++ -o dia05_1 dia05_1.cpp
 * Ejecutar: ./dia05_1 < input.txt
 */

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;
/* ****************************************** */
/* Estructuras de datos a usar como variables globales */
vector<long> seeds;

/* En cada vector de este vector:
    [0] -> destination initial
    [1] -> source initial
    [2] -> range
 */
vector<vector<vector<long>>> veins; //Lista con todas las tranformaciones
/* ****************************************** */

long lowest_loc_num(){
    long semilla_actual,source_actual,destination_actual;
    /* Para cada una de las semillas aplico transformaciones */
    for(int i = 0; i <= seeds.size(); i++){
        semilla_actual = seeds[i];
        for(int j = 0; j < veins.size(); j++){
            for(int k = 0; k < veins[j].size(); k++){
                source_actual = veins[j][k][1]; destination_actual = veins[j][k][0];

                if(semilla_actual >= source_actual && semilla_actual <= veins[j][k][2] + source_actual){
                    semilla_actual = destination_actual + (semilla_actual - source_actual);
                    break;
                }
            }
        }
        seeds[i] = semilla_actual;
    }

    auto min_it = std::min_element(seeds.begin(), seeds.end());
    // Verificar que no estemos devolviendo el final del vector antes de devolver el valor mínimo
    return min_it == seeds.end()? -1 : *min_it;
}


void read_input(){
    string linea, ignore;
    long n;

    /* SEMILLAS */
    getline(cin, linea);
    istringstream iss(linea);
    iss >> ignore;
    while(iss >> n) seeds.push_back(n);

    /* TRANSFORMACIONES */
    getline(cin, linea); getline(cin, linea);

    while(getline(cin, linea)){
        vector<vector<long>> something_to_something;
        while(!linea.empty()){
            istringstream iss(linea);
            vector<long> trans;
            while(iss >> n) trans.push_back(n);
            something_to_something.push_back(trans);
            getline(cin, linea);
        }
        veins.push_back(something_to_something);
        getline(cin, linea); 
    }
}

int main(){
    read_input();
    cout << "Lowest 'location number': " << lowest_loc_num() << endl;
    return 0;
}
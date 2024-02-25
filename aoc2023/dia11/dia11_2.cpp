/**
 * Compilar: g++ -o dia11_2 dia11_2.cpp
 * Ejecutar: ./dia11_2 < input.txt
 */

#include <iostream>
#include <vector>
#include <algorithm>

#define EXPANSION 1000000 // Valor de expansion (la distancia es EXPANSION veces mas grande)

using namespace std;

/* Se usa la distancia de Manhattan */
int distancia_entre_galaxias(pair<int, int> g1, pair<int, int> g2){
    return abs(g1.first - g2.first) + abs(g1.second - g2.second);
}
/* ******************************************** */
/* Estructuras de datos como variables globales */
vector<vector<char>> universe; // Matriz que representa el universo (dado como input)
/* Para guardar el numero de fila/columna que necesitan expansion */
vector<int> filas_expandidas;
vector<int> columnas_expandidas;
/* ******************************************** */

vector<pair<int, int>> localizacion_galaxias(){
    vector<pair<int, int>> galaxias;
    for (int i = 0; i < universe.size(); i++){
        for (int j = 0; j < universe[i].size(); j++){
            if (universe[i][j] == '#'){
                galaxias.push_back(make_pair(i, j));
            }
        }
    }
    return galaxias;
}

bool fila_o_columna_vacia(int n, bool esFila){
    if (esFila){
        for (int j = 0; j < universe[n].size(); j++){
            if (universe[n][j] == '#') return false;
        }
    } else {
        for (int i = 0; i < universe.size(); i++){
            if (universe[i][n] == '#') return false;
        }
    }
    return true;  
}

void expand_universe(){
    for (int i = 0; i < universe.size(); i++){
        if (fila_o_columna_vacia(i, true)){
            filas_expandidas.push_back(i);
        }
    }

    for (int i = 0; i < universe[0].size(); i++){
        if (fila_o_columna_vacia(i, false)){
            columnas_expandidas.push_back(i);
        }
    }
}

void read_input(){
    string linea;
    while (getline(cin, linea)){
        vector<char> fila;
        for (char c : linea) fila.push_back(c);
        universe.push_back(fila);
    }    
}

long suma_distancias(){
    vector<pair<int, int>> galaxias = localizacion_galaxias();
    int cuenta_expansiones;

    int min_x, max_x, min_y, max_y;

    long suma = 0;
    /* Recorrido de todos los pares de galaxias */
    for (int i = 0; i < galaxias.size(); i++){
        for (int j = i+1; j < galaxias.size(); j++){
            
            cuenta_expansiones = 0;

            min_x = min(galaxias[i].first, galaxias[j].first);
            max_x = max(galaxias[i].first, galaxias[j].first);
            min_y = min(galaxias[i].second, galaxias[j].second);
            max_y = max(galaxias[i].second, galaxias[j].second);

            /* Calculo numero de expansiones por filas */
            for(int i = min_x; i <= max_x; i++){
                if(find(filas_expandidas.begin(), filas_expandidas.end(),i)!= filas_expandidas.end()) cuenta_expansiones++;
            }
            /* Calculo numero de expansiones por columnas */
            for(int i = min_y; i <= max_y; i++){
                if(find(columnas_expandidas.begin(), columnas_expandidas.end(), i) != columnas_expandidas.end()) cuenta_expansiones++;
            }
        
            suma += distancia_entre_galaxias(galaxias[i], galaxias[j]) + cuenta_expansiones*(EXPANSION - 1); // Se resta 1 porque la cuenta de expansiones incluye la galaxia
        }
    }
    return suma;
}

int main() {
    string linea;
    read_input();
    expand_universe();

    long suma_d_galaxias = suma_distancias();
    cout << "Suma distancias entre galaxias: " << suma_d_galaxias << endl;

    return 0;
}  
/**
 * Compilar: g++ -o dia11_1 dia11_1.cpp
 * Ejecutar: ./dia11_1 < input.txt
 */

#include <iostream>
#include <vector>

using namespace std;

/* Se usa la distancia de Manhattan */
int distancia_entre_galaxias(pair<int, int> g1, pair<int, int> g2){
    return abs(g1.first - g2.first) + abs(g1.second - g2.second);
}
/* ******************************************** */
/* Estructuras de datos como variables globales */
vector<vector<char>> universe;
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
    vector<vector<char>> new_universe;
    
    /* Insercion de filas */
    for (int i = 0; i < universe.size(); i++){
        if (fila_o_columna_vacia(i, true)){
            new_universe.push_back(universe[i]);
        }
        new_universe.push_back(universe[i]);
    }

    /* Insercion de columnas */
    for (int i = 0; i < new_universe.size(); i++){
        vector<char> fila;
        for (int j = 0; j < new_universe[i].size(); j++){
            if (fila_o_columna_vacia(j, false)){
                fila.push_back(new_universe[i][j]);
            }
            fila.push_back(new_universe[i][j]);
        }
        new_universe[i] = fila;
    }

    universe = new_universe;
}

void read_input(){
    string linea;
    while (getline(cin, linea)){
        vector<char> fila;
        for (char c : linea){
            fila.push_back(c);
        }
        universe.push_back(fila);
    }    
}

int suma_distancias(){
    vector<pair<int, int>> galaxias = localizacion_galaxias();
    int suma = 0;
    for (int i = 0; i < galaxias.size(); i++){
        for (int j = i+1; j < galaxias.size(); j++){
            suma += distancia_entre_galaxias(galaxias[i], galaxias[j]);
        }
    }
    return suma;
}

int main() {
    string linea;
    read_input();
    expand_universe();

    int suma_d_galaxias = suma_distancias();
    cout << "Suma distancias entre galaxias: " << suma_d_galaxias << endl;

    return 0;
}  
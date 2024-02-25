/**
 * Compilar: g++ -o dia03_2 dia03_2.cpp
 * Ejecutar: ./dia03_2 < input.txt
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<char>> schema;
/* en cada uno de los elementos de este vector:
    [0] -> fila
    [1] -> columna
    [2] -> part numbers adyacentes
    [3] -> gear ratio
*/
vector<vector<int>> simbolos_info;

bool is_symbol(char c){ return c != '.' && !isdigit(c); }

int schema_to_int(int fila, int ini, int fin){
    int ret = 0;

    while(ini <= fin) {
        ret = ret * 10 + (schema[fila][ini] - '0');
        ini++;
    }
    return ret;
}

void simbolos(){
    for(int i = 0; i < schema.size(); i++){
        for(int j = 0; j < schema[i].size(); j++){
            if(is_symbol(schema[i][j])){
                simbolos_info.push_back({i, j, 0, 1});
            }
        }
    }
}

// devuelve el valor del "gear ratio" en la posición pos en caso de haber dos part numbers exactamente adyacentes
void gear_ratios(){
    int ini_num, fin_num, valor;

    /* Recorrer schema */
    for(int i = 0; i < schema.size(); i++){
        for(int j = 0; j < schema[i].size(); j++){
            if(isdigit(schema[i][j])){
                ini_num = j, fin_num = ini_num; 
                while(++j < schema[i].size() && isdigit(schema[i][j])){ fin_num++;} // Buscar el final del número
                valor = schema_to_int(i, ini_num, fin_num);

                for(int k = ini_num - 1; k < fin_num + 2; k++){
                    for(int l = i - 1; l < i + 2; l++){
                        if(l < 0 || l >= schema.size() || k < 0 || k >= schema[l].size()){ continue; } // Si se sale del esquema, no se comprueba
                        if(is_symbol(schema[l][k])){ // Si es un símbolo, se busca en simbolos_info
                            for(int m = 0; m < simbolos_info.size(); m++ ){
                                if(simbolos_info[m][0] == l && simbolos_info[m][1] == k){
                                    simbolos_info[m][2]++;
                                    simbolos_info[m][3] *= valor;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

/* Si el numero 'part numbers' adyacentes es exactamente 2 se añade el gear ratio al total */
long calcular_suma(){
    long suma = 0;
    for (int i = 0; i < simbolos_info.size(); i++){
        if(simbolos_info[i][2] == 2) suma += simbolos_info[i][3];
    }
    return suma;
}

void read_input(){
    string linea;
    while (getline(cin, linea)){
        vector<char> fila;
        for (char c : linea) fila.push_back(c);
        schema.push_back(fila);
    }    
}

int main(){
    read_input();
    simbolos();
    gear_ratios();

    cout << "Suma \"gear ratios\": " << calcular_suma() << endl;

    return 0;
}
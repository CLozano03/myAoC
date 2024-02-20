/**
 * Compilar: g++ -o dia03_2 dia03_2.cpp
 * Ejecutar: ./dia03_2 < input.txt
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define SCHEMA_TAM 140

std::vector<std::vector<char>> leer_entrada(){
    std::vector<std::vector<char>> ret(140, std::vector<char>(140)); 
    string linea;
    int n_linea = 0;

    while(!std::cin.eof()){
        getline(cin, linea);

        for(int j = 0; j < SCHEMA_TAM; j++){
            ret[n_linea][j] = linea[j];
        }
        n_linea++;
    }
    return ret;
}

bool is_symbol(char c){
    return c != '.' && !isdigit(c);
}

int schema_to_int(std::vector<std::vector<char>> schema, int fila, int ini, int fin){
    int ret = 0;

    while(ini <= fin) {
        ret = ret * 10 + (schema[fila][ini] - '0');
        ini++;
    }
    return ret;
}

// devuelve el valor del "gear ratio" en la posición pos en caso de haber dos part numbers exactamente adyacentes
int gear_ratio(std::vector<std::vector<char>> schema, pair<int, int> pos){
    int fila = pos.first; int columna = pos.second;
    int cuenta_part_numbers = 0;

    if(isdigit(schema[fila][columna - 1])){ cuenta_part_numbers++; }
    if(isdigit(schema[fila][columna + 1])){ cuenta_part_numbers++; }
    if(isdigit(schema[fila -1][columna - 1])){ 
        cuenta_part_numbers++; 
        if(!isdigit(schema[fila -1][columna] ) && isdigit(schema[fila -1][columna + 1])){ cuenta_part_numbers++; }
    } else if(isdigit(schema[fila -1][columna]) || schema[fila -1][columna + 1]){ cuenta_part_numbers++; }

    if(isdigit(schema[fila + 1][columna - 1])){ 
        cuenta_part_numbers++; 
        if(!isdigit(schema[fila  + 1][columna]) && isdigit(schema[fila + 1][columna + 1])){ cuenta_part_numbers++; }
    } else if(isdigit(schema[fila + 1][columna]) || schema[fila + 1][columna + 1]){ cuenta_part_numbers++; }
    

    if(cuenta_part_numbers != 2){ return 0; } // Si no hay dos part numbers exactamente adyacentes, no se hace nada

    return 1;
}


int calcular_suma(std::vector<std::vector<char>> schema){
    int suma = 0;
    int n_linea = 0;

    int inicio_numero;

    //Filas del esquema
    for(n_linea = 0; n_linea < SCHEMA_TAM; n_linea++){

        for(int j = 0; j < SCHEMA_TAM; j++){
            if(is_symbol(schema[n_linea][j]) && n_linea == 2){ suma += 0;
            if(gear_ratio(schema, make_pair(n_linea, j)) == 1){
                cout << "gR " << n_linea << ", " << j << " Simbolo: " << schema[n_linea][j] << endl;
            }}
        }
    }
    return suma;
}

int main(){

    std::vector<std::vector<char>> schema = leer_entrada();
    int gear_ratio_sum =  calcular_suma(schema);  

    cout << "Suma \"gear ratios\": " << gear_ratio_sum << endl;

    return 0;
}
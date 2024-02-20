/**
 * Compilar: g++ -o dia03_1 dia03_1.cpp
 * Ejecutar: ./dia03_1 < input.txt
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

int schema_to_int(vector<vector<char>> schema, int fila, int ini, int fin){
    int ret = 0;

    while(ini <= fin) {
        ret = ret * 10 + (schema[fila][ini] - '0');
        ini++;
    }
    return ret;
}

bool es_part_number(vector<vector<char>> schema, int fila, int ini, int fin){
    bool ret = false;

    for(int f = fila - 1; f <= fila + 1 && !ret; f++){
        if(f < 0 || f >= SCHEMA_TAM){ continue; } // Si se sale del esquema, no se comprueba
        for(int c = ini -1; c <= fin + 1 && !ret; c++){
            if(c < 0 || c >= SCHEMA_TAM){ continue; } // Si se sale del esquema, no se comprueba
            
            if(is_symbol(schema[f][c])){ ret = true; }
        }
    }
    return ret;
}


int calcular_suma(std::vector<std::vector<char>> schema){
    int suma = 0;
    int n_linea = 0;

    int inicio_numero;

    //Filas del esquema
    for(n_linea = 0; n_linea < SCHEMA_TAM; n_linea++){

        for(int j = 0; j < SCHEMA_TAM; j++){
            if(isdigit(schema[n_linea][j])){
                inicio_numero = j;

                while(j < SCHEMA_TAM && isdigit(schema[n_linea][j])){ j++; } // Buscar el final del número

                if(es_part_number(schema, n_linea, inicio_numero, j - 1)){
                    suma += schema_to_int(schema, n_linea, inicio_numero, j - 1);
                }
            }   
        }
    }
    return suma;
}

int main(){

    std::vector<std::vector<char>> schema = leer_entrada();

    int part_num_sum =  calcular_suma(schema);  

    cout << "Suma \"part numbers\": " << part_num_sum << endl;

    return 0;
}
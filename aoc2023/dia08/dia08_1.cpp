/**
 * Compilar: g++ -o dia08_1 dia08_1.cpp
 * Ejecutar: ./dia08_1 < input.txt
 */

#include <iostream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

// Estructuras de datos declaradas globalmente para evitar pasarlas como argumentos
string instructions;
map<string, pair<string,string>> mapa;


void read_input(){
    string linea;

    getline(cin, linea); 
    instructions = linea;
    string key, value1, value2;

    getline(cin, linea); // Se lee la linea en blanco

    while(getline(cin, linea)){
        //Todos tienen misma longitud, lo cogemos como substring
        key = linea.substr(0,3);
        value1 = linea.substr(7,3);
        value2 = linea.substr(12,3);
        mapa[key] = make_pair(value1, value2);
    }

}

string select_LR(char c, pair<string,string> p){
    return c == 'L' ? p.first : p.second;
}

int number_of_steps(){
    int contador = 0;
    const int INSTR_TAM = instructions.size();
    string actual = "AAA";
    // Se asume por el enunciado que hay siempre una solucion
    while(actual != "ZZZ"){
        actual = select_LR(instructions[contador % INSTR_TAM], mapa[actual]);
        contador++;
    }

    return contador;
}

int main() {
    int res;
    read_input();

    res = number_of_steps();
    cout << "El numero de pasos para llegar a \"ZZZ\" es: "<< res << endl;

    return 0;
}
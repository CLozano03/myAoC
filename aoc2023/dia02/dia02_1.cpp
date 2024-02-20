/**
 * Compilar: g++ -o dia02_1 dia02_1.cpp
 * Ejecutar: ./dia02_1 < input.txt
 */

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

#define MAX_RED 12
#define MAX_GREEN 13
#define MAX_BLUE 14

int suma_ids(){
    const std::string::size_type NPOS = std::string::npos;

    string linea, color, sacado;
    int n_juego, n_sacados;
    size_t ini, fin, pos_punto_y_coma;
    int contador = 0;
    bool flag_imposible, exit_while;

    while (!std::cin.eof()) {
        flag_imposible = false; exit_while = false;
        getline(cin, linea);
    
        ini = linea.find("Game") + 5; //5 caracteres para saltar "Game "
        fin = linea.find(":", ini);
        // Numero de juego
        n_juego = stoi(linea.substr(ini, fin - ini));
        ini = fin + 1;

        // Lectura de los juegos
        pos_punto_y_coma = linea.find(";", ini); 
        while (!exit_while) {

            if (pos_punto_y_coma == NPOS) {
                pos_punto_y_coma = linea.size();
                exit_while = true;
            }
            sacado = linea.substr(ini, pos_punto_y_coma - ini); // Extraer los sacados (hasta ;)   

            std::istringstream iss(sacado);

            while (iss >> n_sacados >> color) {
                if(color.back() == ',') {color.pop_back();} // Eliminar la coma del final

                if ( (color == "red" && n_sacados > MAX_RED) || 
                     (color == "green" && n_sacados > MAX_GREEN) || 
                     (color == "blue" && n_sacados > MAX_BLUE)){
                    flag_imposible = true;
                    break;
                }
            }
            if (flag_imposible) {break;}

            ini = pos_punto_y_coma + 1;
            pos_punto_y_coma = linea.find(";", ini);
        } 
        //Se ha terminado de leer la linea y se comprueba si es posible
        if (!flag_imposible) {contador += n_juego;}}
    return contador;
}


int main(){
    int juegos_posibles = suma_ids();
    cout << "Suma ids de juegos posibles: " << juegos_posibles << endl;

    return 0;
}
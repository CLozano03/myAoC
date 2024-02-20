/**
 * Compilar: g++ -o dia02_2 dia02_2.cpp
 * Ejecutar: ./dia02_2 < input.txt
 */

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int calcular_potencias(){
    const std::string::size_type NPOS = std::string::npos;

    string linea, color, sacado;
    int max_red, max_green, max_blue, n_sacados;
    size_t ini, fin, pos_punto_y_coma;
    int contador = 0;
    bool exit_while;

    while (!std::cin.eof()) {
        flag_imposible = false; exit_while = false;
        max_red = 0; max_green = 0; max_blue = 0;
        getline(cin, linea);
    
        ini = linea.find(":") + 1; //Se empieza a leer despues de los dos puntos

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

                if (color == "red" && n_sacados > max_red) {max_red = n_sacados;}
                if (color == "green" && n_sacados > max_green) {max_green = n_sacados;}
                if (color == "blue" && n_sacados > max_blue) {max_blue = n_sacados;}
            }

            ini = pos_punto_y_coma + 1;
            pos_punto_y_coma = linea.find(";", ini);
        } 
        //Se ha terminado de leer la linea 
        contador += max_red * max_green * max_blue;
    }
    return contador;
}


int main(){
    int suma_potencias = calcular_potencias();
    cout << "Suma 'potencias' de cada juego: " << suma_potencias << endl;

    return 0;
}
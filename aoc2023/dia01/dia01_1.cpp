/**
 * Compilar: g++ dia01_1.cpp -o dia01_1 -g
 * Ejecutar: ./dia01_1 < input.txt
 */

#include <iostream>

using namespace std;

int calcular() {
    string linea;
    int contador = 0;
    int digito1, digito2;

    while (getline(cin, linea)) {
        digito1 = -1;
        digito2 = -1;

        // Iterar sobre cada carácter de la línea
        for (char c : linea) {
            if (isdigit(c)) {
                if (digito1 == -1) {
                    digito1 = c - '0';
                }
                digito2 = c - '0';
            }
        }

        // Si ambos dígitos se han encontrado, sumarlos al contador
        if (digito1 != -1 && digito2 != -1) contador += (digito1 * 10 + digito2);
    }
    return contador;
}

int main() {
    cout << "Suma de los valores de calibre: " << calcular() << endl;
    return 0;
}
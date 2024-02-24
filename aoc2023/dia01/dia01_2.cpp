/**
 * Compilar: g++ dia01_2.cpp  -o dia01_2 -g
 * Ejecutar: ./dia01_2 < input.txt
 */

#include <iostream>
#include <map> 
#include <string>

using namespace std;

bool endsWith(const std::string& fullString, const std::string& ending) {
    if (fullString.length() >= ending.length()) {
        return (0 == fullString.compare(fullString.length() - ending.length(), ending.length(), ending));
    } else {
        return false;
    }
}

map<string, int> dict = {
    {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4},
    {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8},
    {"nine", 9}
};

bool esNumero(char c) { return c >= '0' && c <= '9'; }

int calcular() {
    int contador = 0;
    int digito1, digito2;
    string linea, buffer, aux;

    while (getline(cin, linea)) {
        digito1 = -1;
        buffer.clear();

        for (char c : linea) {
            if (isdigit(c)) {
                buffer.clear();
                if (digito1 == -1) digito1 = c - '0';
                digito2 = c - '0';
            } else {
                buffer.push_back(c);
                for (auto it = dict.begin(); it != dict.end(); ++it) {
                    if (endsWith(buffer, it->first)) {
                        buffer = it->first;
                        break;
                    }
                }
                
                if(dict.find(buffer) == dict.end()) continue;               
                if (digito1 == -1) digito1 = dict[buffer];    
                digito2 = dict[buffer];
            }

        }
        if (digito1 != -1 && digito2 != -1) contador += digito1 * 10 + digito2;
    }
    return contador;
}

int main() {
    cout << calcular() << endl;
    return 0;
}

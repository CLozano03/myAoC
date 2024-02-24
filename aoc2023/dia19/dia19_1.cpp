/**
 * Compilar: g++ -o dia19_1 dia19_1.cpp
 * Ejecutar: ./dia19_1 < input.txt
 */

#include <iostream>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

/* Metodo split auxiliar para dividir las comas */
std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

/* Metodo auxiliar para sumar elementos de un vector de int */
int suma_vector(vector<int> v){
    int suma = 0;
    for (int i = 0; i < v.size(); i++) suma += v[i];
    return suma;
}

class Workflow{
    public:
        string nombre;
        vector<string> rules;
        Workflow(){}
        Workflow(string nombre, vector<string> rules){
            this->nombre = nombre;
            this->rules = rules;
        }

        string calcular_respuesta(vector<int>const &part) const{
            int pos_comp, pos_else, pos_part_vec, n_comp;
            string respuesta;

            for (string rule : rules){

                pos_else = rule.find(":");
                if (pos_else == string::npos) return rule;
                respuesta = rule.substr(pos_else+1, rule.size()-pos_else-1);
                pos_part_vec = calcular_pos_part_vec(rule[0]);

                n_comp = stoi(rule.substr(2, pos_else-2));

                if((pos_comp = rule.find(">")) != string::npos){
                    if(part[pos_part_vec] > n_comp) { return respuesta; } else { continue; }
                } else if ((pos_comp = rule.find("<")) != string::npos){
                    if(part[pos_part_vec] < n_comp)  { return respuesta; } else { continue; }
                } else {
                    return rule;
                }
            }

            return respuesta;
        }
    private:
        /* XMAS */
        int calcular_pos_part_vec(char c) const{
            switch(c){
                case 'x': return 0;
                case 'm': return 1;
                case 'a': return 2;
                case 's': return 3;
            }
            return 4;
        }
};

/* ******************************************** */
/* Estructuras de datos como variables globales */
vector<vector<int>> parts;
map<string, Workflow> workflows;
/* ******************************************** */
void read_input(){
    string linea, nombre_wf, rules;
    vector<string> rules_vect;
    char ignorar;
    int n;

    /* Lectura de los workflow */
    getline(cin, linea);
    while(!linea.empty()){
        rules_vect.clear();

        n = linea.find("{");
        nombre_wf = linea.substr(0, n);
        rules = linea.substr(n+1, linea.size()-n-2); // Quitar las llaves


        for (string rule : split(rules, ',')){
            rules_vect.push_back(rule);
        }

        workflows.insert(make_pair(nombre_wf, Workflow(nombre_wf, rules_vect)));

        getline(cin, linea);
    }

    /* Lectura de las 'parts'*/
    while(getline(cin, linea)){
        vector<int> part;
        istringstream iss(linea);

        for (int i = 0;i < 4; i++){
            iss >> ignorar >> ignorar >> ignorar >> n;
            part.push_back(n);
        }
        parts.push_back(part);
    }

}

/* Manejador principal de la solucion */
int suma_ratings_partsA(){
    int suma = 0;
    string actual, respuesta;

    for (vector<int> part : parts){
        actual = "in";

        while(actual != "A" && actual != "R"){
            Workflow wf_actual = workflows[actual];
            actual = wf_actual.calcular_respuesta(part);
        }

        /* Si la 'part' ha sido aceptada se suman los enteros del vector */
        if (actual == "A")suma += suma_vector(part);
    }

    return suma;
}

int main() {
    string linea;
    read_input();
    int suma_partsA = suma_ratings_partsA();

    cout << "Suma ratings 'parts' aceptadas: " << suma_partsA << endl;

    return 0;
}  
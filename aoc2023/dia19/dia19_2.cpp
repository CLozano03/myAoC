/**
 * Compilar: g++ -o dia19_2 dia19_2.cpp
 * Ejecutar: ./dia19_2 < input.txt
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
};

/* ******************************************** */
/* Estructuras de datos como variables globales */
map<string, Workflow> workflows;
/* ******************************************** */
void read_input(){
    string linea, nombre_wf, rules;
    vector<string> rules_vect;
    char ignorar;
    int n;

    /* Lectura de los workflow Ahora solo interesa esa parte */
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
}



int main() {
    string linea;
    read_input();
    unsigned long suma_partsA = suma_ratings_partsA();

    cout << "Suma ratings 'parts' aceptadas: " << suma_partsA << endl;

    return 0;
}  
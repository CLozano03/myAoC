/**
 * Compilar: g++ -o dia09_1 dia09_1.cpp
 * Ejecutar: ./dia09_1 < input.txt
 */

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

long next_val_aux(vector<long>& v, vector<long>& next);

bool all_0(const vector<long>& v){
    for(int i : v){if(i != 0) return false; }
    return true;
}

vector<long>& next_vector(vector<long>& v){
    vector<long>& next = *new vector<long>();
    for (int i = 0; i < v.size() - 1; i++){
            next.push_back(v[i + 1] - v[i]);
    }
    return next;
}


long next_val(vector<long>& v){
    return next_val_aux(v, next_vector(v));
}

long next_val_aux(vector<long>& v, vector<long>& next){
    if(all_0(next)) return v.back();
    else return v.back() + next_val_aux(next, next_vector(next));
}

int main() {
    string linea;
    int n;
    long suma_next_vals = 0;

    while(getline(cin, linea)){
        vector<long> v;
        istringstream iss(linea);
        while(iss >> n){
            v.push_back(n);
        }

        suma_next_vals += next_val(v);
    }

    cout << "Suma de next_values: " << suma_next_vals << endl;
    


    return 0;
}  
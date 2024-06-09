#include <iostream>
#include <sstream>

#define MAP_SIZE 140
#define MAX_INT 7000

char pipes_map[MAP_SIZE][MAP_SIZE];
std::pair<int, int> start_pos;


enum Direction {UP, DOWN, LEFT, RIGHT};


int path_map[MAP_SIZE][MAP_SIZE];


void initialize_path_map() {
    for (int i = 0; i < MAP_SIZE; ++i) {
        for (int j = 0; j < MAP_SIZE; ++j) {
            path_map[i][j] = MAX_INT;
        }
    }
}

void paths_from(std::pair<int, int> currentPos, int distance, Direction dir){
    /* 
                     UP

            Left    Current   Right

                     DOWN
    
     */

    int x = currentPos.first; int y = currentPos.second;
    int previous_distance;

    Direction next_dir; // Next direction to move depending on the pipe of the next cell


    /* Taking the next direction to move */
    switch (dir)
    {
    case UP:
        if (x - 1 < 0){ break; }
        
        switch (pipes_map[x - 1][y])
        {
        case '|':
            next_dir = UP; break;
        case 'F':
            next_dir = RIGHT; break;
        case '7':
            next_dir = LEFT; break;
        default:
            throw std::invalid_argument("Invalid pipe where dir was: " + std::to_string(dir));
        }

        previous_distance = path_map[x - 1][y];
        path_map[x - 1][y] = std::min(previous_distance, distance + 1);
        if (previous_distance == path_map[x-1][y]){ break; }


        paths_from(std::make_pair(x - 1, y), distance + 1, next_dir);

        break;
    case DOWN:
        if (x + 1 >= MAP_SIZE){ break; }

        switch (pipes_map[x + 1][y])
        {
        case '|':
            next_dir = DOWN; break;
        case 'L':
            next_dir = RIGHT; break;
        case 'J':
            next_dir = LEFT; break;
        default:
            throw std::invalid_argument("Invalid pipe where dir was: " + std::to_string(dir));
        }
        previous_distance = path_map[x + 1][y];
        path_map[x + 1][y] = std::min(previous_distance, distance + 1);
        if (previous_distance == path_map[x+1][y]){ break; }

        paths_from(std::make_pair(x + 1, y), distance + 1, next_dir);


        break;
    case LEFT:
        if (y - 1 < 0){ break; }

        switch (pipes_map[x][y -1])
        {
        case '-':
            next_dir = LEFT; break;
        case 'L':
            next_dir = UP; break;
        case 'F':
            next_dir = DOWN; break;
        default:
            throw std::invalid_argument("Invalid pipe where dir was: " + std::to_string(dir));
        }
        previous_distance = path_map[x][y - 1];
        path_map[x][y - 1] = std::min(previous_distance, distance + 1);
        if (previous_distance == path_map[x][y - 1]){ break; }

        paths_from(std::make_pair(x, y - 1), distance + 1, next_dir);

        break;
    case RIGHT:
        if (y + 1 >= MAP_SIZE){ break; }

        switch (pipes_map[x][y  + 1])
        {
        case '-':
            next_dir = RIGHT; break;
        case 'J':
            next_dir = UP; break;
        case '7':
            next_dir = DOWN; break;
        default:
            throw std::invalid_argument("Invalid pipe where dir was: " + std::to_string(dir));
        }

        previous_distance = path_map[x][y + 1];
        path_map[x][y + 1] = std::min(previous_distance, distance + 1);
        if (previous_distance == path_map[x][y + 1]){ break; }

        paths_from(std::make_pair(x, y + 1), distance + 1, next_dir);

        break;
    default:
        throw std::invalid_argument("Invalid direction");
    }

}

/* Stores input in pipes_map matrix */
void read_input(){
    char c;

    for (int i = 0; i < MAP_SIZE; i++){
        for (int j = 0; j < MAP_SIZE; j++){
            std::cin >> c;

            if (c == 'S'){
                start_pos = std::make_pair(i, j);
            }

            pipes_map[i][j] = c;
        }
    }
}

int take_largest_path(){
    int max_path = 0;

    for (int i = 0; i < MAP_SIZE; i++){
        for (int j = 0; j < MAP_SIZE; j++){
            if (path_map[i][j] == MAX_INT) continue;
            max_path = std::max(max_path, path_map[i][j]);
        }
    }
    return max_path;
}

void print_path_map(){
    for (int i = 0; i < MAP_SIZE; i++){
        for (int j = 0; j < MAP_SIZE; j++){
            std::cout << path_map[i][j] << "   \t";
        }
        std::cout << std::endl;
    }
}

int main(){
    read_input();  

    initialize_path_map(); 

    paths_from(start_pos, 0, UP);
    paths_from(start_pos, 0, DOWN);
    print_path_map();

    int max_path = take_largest_path();
    
    std::cout << std::endl << "====================" << std::endl << "Max path: " << max_path << std::endl;

    return 0;
}
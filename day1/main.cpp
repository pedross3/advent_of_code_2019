#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<int> loadFile(const std::string &filename)
{
    std::ifstream file(filename);
    std::vector<int> data;
    std::string line;
    while (std::getline(file, line))
    {
        if (!line.empty())
        {
            data.push_back(std::stoi(line));
        }
    }
    return data;
}

int calculate_fuel(int value) {
    return value / 3 - 2;
}

int main() {
    std::vector<int> whole_module = loadFile("input.txt");
    int total = 0;

    for (int module_line : whole_module) {
        int fuel = calculate_fuel(module_line);

        while (fuel > 0) {
            total += fuel;
            fuel = calculate_fuel(fuel);
        }
    }

    std::cout << "Total: " << total << "\n";

    return 0;
}

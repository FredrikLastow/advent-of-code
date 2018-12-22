#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
  ifstream inputFile;
  inputFile.open("input.txt");

  if (!inputFile) {
    cerr << "Error";
    exit(1);
  } else {
    string s = "";
    string ids [250] = { };
    int doubbleCount = 0;
    int trippleCount = 0;
    int asd = 1;
    int hasDouble;
    int hasTripple;
    int foundCount;

    int length = 0;
    while (inputFile >> s) {
      ids[length] = s;
      length++;
    }

    for(int j = 0; j < length - 1; j++) {
      cout << strcmp(ids[j], ids[j+1]);
    }

    cout << doubbleCount*trippleCount << "\n";
  }
  return 0;
}

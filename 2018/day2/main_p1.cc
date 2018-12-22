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
    int doubbleCount = 0;
    int trippleCount = 0;
    int asd = 1;
    int hasDouble;
    int hasTripple;
    int foundCount;

    while (inputFile >> s) {
      hasDouble = 0;
      hasTripple = 0;

      for(int i = 0; i < s.size() - 1; i++) {
        foundCount = 0;

        if (s[i] != '0') {
          for(int j = i + 1; j < s.size(); j++) {
            if(s[i] == s[j]) {
              s[j] = '0';
              foundCount++;
            }
          }
        }

        if(foundCount == 1 && !hasDouble) {
          hasDouble = 1;
          doubbleCount++;
        }

        if(foundCount == 2 && !hasTripple) {
          hasTripple = 1;
          trippleCount++;
        }
      }
    }

    cout << doubbleCount*trippleCount << "\n";
  }
  return 0;
}

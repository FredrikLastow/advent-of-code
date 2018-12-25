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

    int length = 0;
    while (inputFile >> s) {
      ids[length] = s;
      length++;
    }

    for(int i = 0; i < length - 1; i++) {
      string id = ids[i];
      for(int j = i; j < length; j++) {
        string compId = ids[j];
        int wrongCount = 0;

        for(int k = 0; k < 26; k++) {
          if (id[k] != compId[k]) {
            wrongCount++;
          }
        }

        if (wrongCount == 1) {
          cout << id << "\n";
          cout << compId << "\n";
        }
      }
    }

  }
  return 0;
}

#include <iostream>
#include <fstream>
#include <array>
using namespace std;

int main()
{
  ifstream inputFile;
  inputFile.open("input.txt");

  if (!inputFile) {
    cerr << "Error";
    exit(1);
  } else {
    int freqChanges [986] = { };

    int freqChange;
    int i = 0;

    while (inputFile >> freqChange) {
      freqChanges[i] = freqChange;
      i++;
    }

    int prevFreq [1000000] = { };
    prevFreq[0] = 0;
    int freq = 0;
    int prevFreqLength = 1;
    int index = 0;
    int finished = 0;

    while (!finished) {

      if (index == 986) {
        index = 0;
      }

      freq = freq + freqChanges[index];

      for(int j = 0; j < prevFreqLength; j = j + 1) {
        if (freq == prevFreq[j]) {

          cout << freq << "\n";
          finished = 1;
          break;
        }
      }

      prevFreq[prevFreqLength] = freq;
      index++;
      prevFreqLength++;
    }
  }
  return 0;
}

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int freq;
  int resFreq;
  ifstream inputFile;
  inputFile.open("input.txt");

  if (!inputFile) {
    cerr << "Error";
    exit(1);
  } else {
    while (inputFile >> freq) {
      resFreq = resFreq + freq;
    }
    cout << resFreq;
  }
  return 0;
}

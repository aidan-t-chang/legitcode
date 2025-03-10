#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
#define MAX_N 10

int N, B[MAX_N][MAX_N];

bool color_appears(int c)
{
  for (int i=0; i<N; i++) 
    for (int j=0; j<N; j++)
      if (B[i][j] == c) return true;
  return false;
}

bool on_top_of(int c1, int c2) {
  int top=N, bottom=0, left=N, right=0;
  for (int i=0; i<N; i++) 
    for (int j=0; j<N; j++)
      if (B[i][j] == c2) {
	top = min(top, i);
	bottom = max(bottom, i);
	left = min(left, j);
	right = max(right, j);
      }

  for (int i=top; i<=bottom; i++) 
    for (int j=left; j<=right; j++)
      if (B[i][j] == c1) return true;
  
  return false;
}

int main(void) {
  ifstream fin ("art.in");
  ofstream fout ("art.out");
  fin >> N;
  for (int i=0; i<N; i++) {
    string s;
    fin >> s;
    for (int j=0; j<N; j++)
      B[i][j] = s[j] - '0';
  }

  int answer = 0;
  for (int i=1; i<=9; i++)
    if (color_appears(i)) {
      bool could_be_first = true;
      for (int j=1; j<=9; j++)
	if (j!=i && color_appears(j) && on_top_of(i,j))
	  could_be_first = false;
      if (could_be_first) answer++;
    }
  
  fout << answer << "\n";
  return 0;
}
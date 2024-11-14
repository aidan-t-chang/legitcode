#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int main() {
    freopen("square.in", "r", stdin);
    freopen("square.out", "w", stdout);

    int x1, x2, y1, y2;
    int x3, x4, y3, y4;

    cin >> x1 >> y1 >> x2 >> y2;
    cin >> x3 >> y3 >> x4 >> y4;

    int bottomleft[1];
    int topright[1];

    bottomleft[0] = min(x1, x3);
    bottomleft[1] = min(y1, y3);

    topright[0] = max(x2, x4);
    topright[1] = max(y2, y4);

    int side_length = max((topright[0] - bottomleft[0]), (topright[1] - bottomleft[1]));

    cout << side_length * side_length;
    return 0; 
} 
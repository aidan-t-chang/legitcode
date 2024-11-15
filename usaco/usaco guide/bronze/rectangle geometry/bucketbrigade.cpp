#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
    freopen("buckets.in", "r", stdin);
    freopen("buckets.out", "w", stdout);

    int barn[1]; // x = j, y = i
    int rock[1];
    int lake[1];
    for (int i = 0; i<10; i++) {
        string row;
        cin >> row;

        for (int j = 0; j < 10; j++) {
            if (row[j] == 'B') {
                barn[0] = j;
                barn[1] = i;
            }
            else if (row[j] == 'R') {
                rock[0] = j;
                rock[1] = i;
            } 
            else if (row[j] == 'L') {
                lake[0] = j;
                lake[1] = i;
            } 
        }
    }

    if (barn[0] == lake[0] && lake[0] == rock[0]) {
        if ((barn[1] <= rock[1] && rock[1] <= lake[1]) || (lake[1] <= rock[1] && rock[1] <= barn[1])) {
            cout << (abs(lake[1] - barn[1]) + 1);
        }
        else {
            cout << abs(lake[1] - barn[1]) - 1;
        }
    }
    else if (barn[1] == lake[1] && lake[1] == rock[1]) {
        if ((barn[0] <= rock[0] && rock[0] <= lake[0]) || (lake[0] <= rock[0] && rock[0] <= barn[0])) {
            cout << (abs(lake[0] - barn[0]) + 1);
        }
        else {
            cout << abs(lake[0] - barn[0]) - 1;
        }
    }
    else {
        // return horizontal distance + vertical distance - 1
        cout << (abs(lake[0] - barn[0]) + abs(lake[1] - barn[1]) - 1);
    }
    return 0;
}
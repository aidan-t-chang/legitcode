#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int main() {
    freopen("shell.in", "r", stdin);
    freopen("shell.out", "w", stdout);

    int n; cin >> n;

    vector<pair<int, int>> swaps(n);
    vector<int> guesses(n);

    for (int i = 0; i < n; i++) {
        int a, b, guess; cin >> a >> b >> guess;

        swaps[i] = make_pair(a, b);
        guesses[i] = guess;
    }

    int maxPoints = 0;

    for (int starting = 1; starting <= 3; starting++) {
        vector<bool> hasPebble(4, false);

        hasPebble[starting] = true;

        int cur_points = 0;

        for (int i = 0; i < n; i++) {
            int a = swaps[i].first, b = swaps[i].second;

            swap(hasPebble[a], hasPebble[b]);

            int guess = guesses[i];

            if (hasPebble[guess]) {
                cur_points++;
            }
        }

        maxPoints = max(cur_points, maxPoints);
    }

    cout << maxPoints;

    return 0;
}
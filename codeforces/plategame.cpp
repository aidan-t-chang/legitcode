#include <bits/stdc++.h>
using namespace std;

void solve() {
    int a, b, r;
    cin >> a >> b >> r;

    if (2 * r > min(a, b)) {
        cout << "Second";
    }
    else {
        cout << "First";
    }
}

int main() {
    solve();
}


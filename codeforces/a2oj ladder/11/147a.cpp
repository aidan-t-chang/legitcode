#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    int a, b; cin >> a >> b;
    int count = 0;
    int res = 0;
    for (int i = 0; i < n - 1; i++) {
        int a1, b1; cin >> a1 >> b1;
        if (a == a1 && b == b1) {
             count++;
        }
        else {
            res = max(res, count+1);
            count = 0;
        }
        a = a1;
        b = b1;
    }
    cout << max(res, count+1);
}

int main() {
    solve();
}

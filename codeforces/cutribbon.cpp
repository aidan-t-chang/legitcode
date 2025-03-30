#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, a, b, c;
    cin >> n >> a >> b >> c;

    int res = 0;
    for (int i = 0; i * a <= n; i++) {
        for (int j = 0; i * a + b * j <= n; j++) {
            int remain = n - i * a - b * j;
            if (remain % c == 0) {
                int add = remain / c;
                res = max(res, add + i + j);
            }
        }
    }

    cout << res;
}

int main() {
    solve();
}
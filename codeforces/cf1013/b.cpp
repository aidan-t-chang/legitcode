#include <bits/stdc++.h>
using namespace std;

void solve() {
    // each number larger than x can be in its own team with strength > x
    int n, x;
    cin >> n >> x;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a+n);
    reverse(a, a+n);

    int res = 0;
    for (int i = 0, cnt = 1; i < n; i++, cnt++) {
        if (a[i] * cnt >= x) {
            res++;
            cnt = 0;
        }
    }
    cout << res << endl;
}

int main() {
    int t; cin >> t;
    while (t--) {
        solve();
    }
}

#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    int q; cin >> q;
    map<ll, ll> a;

    while (q--) {
        int t; cin >> t;

        if (t == 0) {
            ll k, v; cin >> k >> v;
            a[k] = v;
        }
        else {
            ll k; cin >> k;
            cout << a[k] << "\n";
        }

    }

    return 0;
}
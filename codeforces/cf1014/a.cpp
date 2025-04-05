#include <bits/stdc++.h>
#include <numeric>
#include <cmath>
using namespace std;

void solve() {
    int n; cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr+n);
    int ab = abs(arr[0] - arr[n-1]);
    cout << ab << endl;
}
int main() {
    int t; cin >> t;
    while (t--) {
        solve();
    }
}

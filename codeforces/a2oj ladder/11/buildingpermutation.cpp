#include <bits/stdc++.h>
using namespace std;


void solve() {
    int n; cin >> n;
    int arr[n];
    long long int res = 0;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr,arr + n); 

    for (int i = 0; i < n; i++) {
        res += abs(arr[i] - i - 1);
    }

    cout << res << endl;
}

int main() {
    solve();
}


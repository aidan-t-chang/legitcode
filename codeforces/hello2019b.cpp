#include <bits/stdc++.h>
using namespace std;

bool dfs(int* arr, int i, int cur, int len) {
    if (i == len && cur % 360 == 0) {
        return true; 
    }
    else if (i == len) {
        return false;
    }
    cur += arr[i];
    i += 1;

    if (dfs(arr, i, cur, len)) {
        return true;
    }
    cur -= arr[i-1];
    cur -= arr[i-1];
    if (dfs(arr, i, cur, len)) {
        return true;
    }
    return false;
}

void solve() {
    int n; cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    if (dfs(arr, 0, 0, n)) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
}

int main() {
    solve();
}

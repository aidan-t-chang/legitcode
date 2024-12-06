#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    freopen("cbarn.in", "r", stdin);
    freopen("cbarn.out", "w", stdout);
    int N; cin >> N;
    int arr[N];
    for (int i = 0; i<N; i++) {
        int temp; cin >> temp;
        arr[i] = temp;
    }

    int res = 999999999;
    for (int i = 0; i<N; i++) {
        int temp = 0;
        for (int j = 0; j<N; j++) {
            if (j < i) {
                temp += (arr[j] * (N - (i-j)));
            }
            else if (i != j) {
                temp += (arr[j] * (j-i));
            }
        }
        res = min(res, temp);
    }
    cout << res;
    return 0;
}
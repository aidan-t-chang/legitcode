#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    int arr[n];
    map<int, int> count; 
    count.insert({0, 3});
    count.insert({2, 2});
    count.insert({1, 1});
    count.insert({3, 1});
    count.insert({5, 1});
    int counter = 8;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
   for (int i = 0; i < n; i++) {
        if (count[arr[i]]){
            count[arr[i]] -= 1;
            counter -= 1;
        }
        if (counter <= 0) { // every character has been counted for
            cout << i+1 << endl;
            break;
        } 
    }
    if (counter > 0) {
        cout << 0 << endl;
    }
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
    solve();
    }
    return 0;
}

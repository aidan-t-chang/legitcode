#include <bits/stdc++.h>
using namespace std;
// legit just mex
void solve() {
	int n; cin >> n;
	int arr[n];
	int news[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	sort(arr, arr+n);
	
	for (int i = 0; i < n; i++) {
		news[i] = i+1;
	}
	
	bool flag = true;
	for (int i = 0; i < n; i++) {
		if (news[i] != arr[i]) {
			cout << i+1 << endl;
			flag = false;
			break;
		}
	}

	if (flag) {
		cout << n+1 << endl;
	}
}

int main() {
	solve();
}

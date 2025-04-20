#include <bits/stdc++.h>
using namespace std;

void solve() {
	// remove any zeroes - guaranteed to make sum smaller?
	string n; cin >> n;
	int count = 0;
	bool flag = false;

	for (int i = n.length()-1; i >= 0; i--) {
		if (n[i] != '0') {
			flag = true;
		}
		else if (flag) {
			count++;
		}
	}
	cout << n.length() - (count + 1) << endl;
	
}

int main() {
	int t; cin >> t;
	while (t--) {
		solve();
	}
}

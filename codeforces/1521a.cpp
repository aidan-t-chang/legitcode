#include <bits/stdc++.h>
using namespace std;

void solve() {
	int a; int b; cin >> a >> b;
	if (b == 1) {
		cout << "NO" << endl;
	}
	else {
		cout << "YES" << endl;
		cout << a << ' ' << a * (long long)b << ' ' << a * ((long long)b + 1) << endl;
	}
}

int main() {
	int t; cin >> t;
	while (t--) {
		solve();
	}
}

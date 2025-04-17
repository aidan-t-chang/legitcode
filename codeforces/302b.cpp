#include <iostream>
using namespace std;
#define ll long long 
#define PB push_back
#define FAST ios::sync_with_stdio(false); cin.tie(nullptr);

int main() {
	FAST;
	ll n, k;
	cin >> n >> k;
	ll m = k;
	if (n % 2 == 0 && n / 2 * n < k) { cout << "NO\n"; return 0; }
	if(n % 2 == 1 && n / 2 * n + (n / 2 + 1) < k) { cout << "NO\n"; return 0; }
	cout << "YES\n"; 
	for (ll i = 0; i < n; i++) {
		for (ll j = 0; j < n; j++) {
			if ((j % 2 == 0 && k != 0 && i % 2 == 0) || (j % 2 == 1 && k != 0 && i % 2 == 1)) { cout << "L"; k--; }
			else { cout << "S"; }
		}
		cout << "\n";
	}
}

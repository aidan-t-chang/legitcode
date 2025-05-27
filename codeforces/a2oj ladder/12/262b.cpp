#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n; int k; cin >> n >> k;

	int arr[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	int i = 0;
	while (k > 0 &&  i < n && arr[i] <= 0){
		arr[i] *= -1;
		k -= 1;
		i++;
	}

	int smallesti = 0;
	int smallestn = arr[0];
	for (int i = 0; i < n; i++) {
		if (abs(arr[i]) < smallestn) {
			smallesti = i;
			smallestn = arr[i];
		}
	}

	if (k % 2 == 1) {
		arr[smallesti] *= -1;
	}

	int sum2 = 0;
	for (int i = 0; i < n; i++) {
		sum2 += arr[i];
	}
	cout << sum2 << endl;
}

int main() {
	solve();
}

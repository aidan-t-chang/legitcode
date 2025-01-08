#include <bits/stdc++.h>
using namespace std;

vector<array<int, 3>> north; // store the cows 
vector<array<int, 3>> east;

int inf = 1e9;

int main() {
    int N; cin>>N;

    vector<pair<int, int>> pos(N);
    for (int i=0;i<N;i++) {
        char d; cin>>d;
        pair<int, int> p;
        cin >> p.first >> p.second;

        array<int, 3> varr = {p.first, p.second, i};
        if (d == 'E') {
            east.push_back(varr);
        }
        else {
            north.push_back(varr);
        }
        pos[i] = p;
    }

    vector<vector<int>> meetTime;
    for (auto nC : north) {
        for (auto eC : east) {
            int yT = eC[1] - nC[1];
            int xT = nC[0] - eC[0];

            if (xT == yT) {
                continue; // differences are the same, the two cows will just pass each other
            }
            
            // time stopped, current cow stopped, and the cow that stopped index 1 cow
            if (yT > xT && xT > 0) {
                meetTime.push_back({yT, nC[2], eC[2], 0});
            }
            else if (yT < xT && yT > 0) {
                meetTime.push_back({xT, eC[2], nC[2], 1});
            }
        }
    }

    sort(meetTime.begin(), meetTime.end());
    vector<int> ans(N, inf);
    for (auto mt : meetTime) {

        if (ans[mt[2]] == inf && ans[mt[1]] == inf) { // both x and y values were not stopped
            ans[mt[1]] = mt[0]; // assign the value of the cow that was stopped the current time
            continue;
        }
        if (ans[mt[1]] == inf) {

            if (mt[3]) {
                int start = pos[mt[2]].second;
                int end = start + ans[mt[2]];

                if (pos[mt[1]].second >= start && pos[mt[1]].second <= end) {
                    ans[mt[1]] = mt[0];
                }
            }
            else {
                int start = pos[mt[2]].first;
                int end = start + ans[mt[2]];

                if (pos[mt[1]].first >= start && pos[mt[1]].first <= end) {
                    ans[mt[1]] = mt[0];
                }
            }
        }
    }

    for (auto res : ans) {
        if (res == inf) {
            cout << "Infinity" << endl;
        }
        else {
            cout << res << endl;
        }
    }
}
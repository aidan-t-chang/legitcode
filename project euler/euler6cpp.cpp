#include <iostream>
#include <cmath>

using namespace std;

int sumsq;
int sum;
const int a = 100;

int main() {
    for (int i = 1; i < a+1; i++) {
        sumsq += i*i;
    }

    for (int i = 1; i < a+1; i++) {
        sum += i;
    }

    cout << sum*sum - sumsq;

    return 0;
}

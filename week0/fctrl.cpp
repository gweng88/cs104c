#include <iostream>

using namespace std;

int main() {
    int num_cases;
    cin >> num_cases;

    int n;
    while (num_cases-- > 0) {
        cin >> n;
        int ans = 0;

        for (int d = 5; d <= n; d *= 5) {
            ans += n / d;
        }

        cout << ans << '\n';
    }

    return 0;
}

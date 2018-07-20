#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<vector<char>> a(n, vector<char>(n, '*'));
  for (int i = 1; i < n - 1; ++i) {
    for (int j = 0; j < n; ++j) {
      if (i + j != n - 1) {
        a[i][j] = ' ';
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cout << a[i][j];
    }
    cout << '\n';
  }
  return 0;
}
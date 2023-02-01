#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N; // The number of tests
    cin >> N;
    for (int t = 0; t < N; t++) {
        char s[100000]; // the string
        cin >> s;
        int lng = strlen(s);
        int min_dels = 0;
        for (int i = 0; i < lng - 1; i++) {
            if (s[i] == s[i+1]) min_dels++;
        }
        cout << min_dels << "\n";
    }
    return 0;
}

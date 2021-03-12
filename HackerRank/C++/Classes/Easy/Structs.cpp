#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

struct Student {
    int age, stnd;
    string first, last;
};

int main() {
    Student s;
    cin >> s.age >> s.first >> s.last >> s.stnd;
    cout << s.age << " " << s.first << " " << s.last << " " << s.stnd;
	return 0;
}

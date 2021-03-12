#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

class Student {
        int age, stnd;
        string first, last;
    public:
        void set_age(int n) {
            age = n;
        }
        void set_first(string s) {
            first = s;
        }
        void set_last(string s) {
            last = s;
        }
        void set_stnd(int n) {
            stnd = n;
        }

        int get_age() {
            return age;
        }
        string get_first() {
            return first;
        }
        string get_last() {
            return last;
        }
        int get_stnd() {
            return stnd;
        }

        string to_string() {
            stringstream ss1, ss2;
            string s1, s2;
            ss1 << age;
            ss1 >> s1;
            ss2 << stnd;
            ss2 >> s2;
            return s1 + "," + first + "," + last + "," + s2;
        }
};

int main() {
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_stnd(standard);
    st.set_first(first_name);
    st.set_last(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last() << ", " << st.get_first() << "\n";
    cout << st.get_stnd() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}

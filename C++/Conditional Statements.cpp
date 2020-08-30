#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    string num_car[]= {"one","two","three","four","five","six","seven","eight","nine"};
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    if (n <=9){
        cout<< num_car[n - 1];
    }
    else{
        cout<<"Greater than 9";
    }

    return 0;
}

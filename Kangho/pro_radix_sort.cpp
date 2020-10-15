#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <queue>
using namespace std;
int c[17];
int digit16(int v, int d){
// 양의 정수 v 의 16진수 d 번째 숫자를 반환하는 함수
// 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 1 이라면 6 을 반환
// 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 4 라면 11 (= 0xb) 을 반환
  v = v >> d*4;
  return v & 0xf;
}

void countingSort16(vector<pair<int, string> >& v,int d){
        vector<pair<int, string> > q(v.size()+1);
        for (int j=0; j<17; j++){
            c[j] = 0;
        }
        for (int j=0; j<v.size(); j++){
            c[digit16(v[j].first, d)]++;
        }
        for (int i=1; i<17; i++){
            c[i] = c[i] + c[i-1];
        }
        for (int j=v.size()-1; j>=0; j--){
            q[c[digit16(v[j].first, d)]] = v[j];
            c[digit16(v[j].first, d)]--;
        }
        for (int k=1; k<v.size()+1; k++){
            v[k-1] = q[k];
        }
};

int main(void) {
    int n;
    vector<pair<int, string> > v;
    cin >> n;
    for (int i=0; i<n; i++){
        int d;
        string s;
        cin >> d >> s;
        v.push_back(pair<int,string>(d,s));
    }
    //radixsort
    for (int d=0; d<8; d++) countingSort16(v, d);

    for (int i=0; i<n; i++){
        cout << v[i].first << ' ' << v[i].second << endl;
    }
    return 0;
}

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int TC;
    cin >> TC;
    while (TC--){
        int N;
        cin >> N;
        vector<string> strs;
        for (int j=0; j<N+1; j++){
            string tmp;
            cin >> tmp;
            strs.push_back(tmp);
        }
        int answer = 0;
        for (int i=1; i<N+1; i++){
            string origin = strs[i-1];
            string target = strs[i];
            int cnt;
            if (i%2 == 0){
                cnt = (origin+origin).find(target);
                answer += cnt;
            }
            else{
                cnt = (target+target).find(origin);
                answer += cnt;
            }
        }
        cout << answer << endl;
    }

    return 0;
}

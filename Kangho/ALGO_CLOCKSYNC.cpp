#include <iostream>
#include <algorithm>
using namespace std;
const int buttons[10][5] = {
        {0, 1, 2 , -1, -1},
        {3, 7, 9, 11, -1},
        {4, 10, 14, 15, -1},
        {0, 4, 5, 6, 7},
        {6, 7, 8, 10, 12},
        {0, 2, 14, 15, -1},
        {3, 14, 15, -1, -1},
        {4, 5, 7, 14, 15},
        {1, 2, 3, 4, 5},
        {3, 4, 5, 9, 13}
};
int currentTime[16];
int ret;
bool noAnswer = true;
void push(int btnIdx, int time){
    for(int i=0; i < 5; i++){
        if (buttons[btnIdx][i] != -1){
            currentTime[buttons[btnIdx][i]] += 3 * time;
        } else break;
    }
}

void push_back(int btnIdx, int time){
    for(int i=0; i < 5; i++){
        if (buttons[btnIdx][i] != -1){
            currentTime[buttons[btnIdx][i]] -= 3 * time;
        } else break;
    }
}

bool check(){
    for (int i=0; i < 16; i++){
        if (currentTime[i] % 12 != 0) return false;
    }
    return true;
}

void syncClock(int buttonIndex){
    if (!noAnswer) return;
    if (check()) {
        cout << ret << endl;
        noAnswer = false;
        return;
    }
    if (buttonIndex > 9) return;
    for (int i=0; i < 4; i++){
        push(buttonIndex, i);
        ret += i;
        syncClock(buttonIndex + 1);
        push_back(buttonIndex, i);
        ret -= i;
    }
    if (!noAnswer) return;
}


int main(void)
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int test_case;
    cin >> test_case;
    for (int i=0; i < test_case; i++){
        for (int j=0; j < 16; j++){
            cin >> currentTime[j];
        }
        ret = 0;
        noAnswer = true;
        syncClock(0);
        if (noAnswer){
            cout << -1 << endl;
        }
    }
    return 0;
}

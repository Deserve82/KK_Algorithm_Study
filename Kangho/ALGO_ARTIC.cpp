#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <iomanip>

using namespace std;

const int INF = 100;
int N;
double dist[INF][INF];
bool decision(double d){
    vector<bool> visited(N, false);
    visited[0] = true;
    queue<int> q;
    q.push(0);
    int check = 0;

    while (!q.empty())
    {
        int here = q.front();
        q.pop();
        ++check;
        for (int there = 0; there<N; there++){
            if (!visited[there] && dist[here][there] <= d)
            {
                visited[there] = true;
                q.push(there);
            }
        }
    }
    return check == N;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int C;
    cin >> C;
    for (int tn = 0; tn < C; ++tn)
    {
        cin >> N;
        vector<pair<double, double> > dis;
        for (int i=0; i< N; i++){
            double a, b;
            cin >> a >> b;
            dis.emplace_back(a, b);
        }
        for(int j=0; j<N; j++)
            for (int k = 0; k < N; k++)
            {
                pair<double, double> point1 = dis[j];
                pair<double, double> point2 = dis[k];
                dist[j][k] = sqrt((point2.first - point1.first)*(point2.first - point1.first) + (point2.second - point1.second)*(point2.second - point1.second));
            }

        double left = 0;
        double right = 1460;
        for (int i=0; i<100; i++){
            double mid = (left + right) / 2;
            if (decision(mid)){
                right = mid;
            } else left = mid;
        }
        cout << fixed << setprecision(2);
        cout << right << endl;
    }
}
// 내가 막혔던 부분, 어떻게 하면 이건 정수로 나눠떨어지는 것도 아닌데 탈출 조건이 되지? - for 문을 돌린다.
// 거리를 저장해야 하나..? 그럼 시간초과 터지는 거 아니야?에 대한 걱정과 고민, 그리고 하나씩 연결을 어떻게 확인하지???? - 거리 저장하는 것이 상식적으로 빠르긴 했지만 나는 다른 획기적인 풀이가 있는 줄 알았다.
// 분명 간단히 해결해던 거 같은데 왜 못했지? - 거리를 따로 저장해 두면 mst나 플로이드도 가능해 진다.

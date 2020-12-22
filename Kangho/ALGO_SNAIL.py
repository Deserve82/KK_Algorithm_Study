def climb(day, climbed, pos):
    if climbed >= depth:
        return pos
    elif day >= days:
        return 0

    if cache[day][climbed] != -1:
        return cache[day][climbed]

    ret = 0
    ret += climb(day + 1, climbed + 2, pos * 0.75)
    ret += climb(day + 1, climbed + 1, pos * 0.25)
    cache[day][climbed] = ret
    return ret


for _ in range(int(input())):
    depth, days = map(int, input().split())
    cache = [[-1]*(depth+1) for _ in range(days+1)]
    print(format(climb(0, 0, 1),".10f"))

# 시간 초과로 c++로 통과하여 작성
# #include <iostream>
# #include <stdio.h>
# 
# using namespace std;
# int depth, days;
# double cache[1001][2001];
# 
# double climb(int day, int climbed, double pos){
#     if (climbed >= depth){
#         return pos;
#     }
#     else if (day >= days) {
#         return 0;
#     }
#     double& ret = cache[day][climbed];
#     if (ret != -1) return ret;
#     ret = 0;
#     ret += climb(day + 1, climbed + 2, pos*0.75);
#     ret += climb(day + 1, climbed + 1, pos*0.25);
#     return ret;
# }
# 
# int main() {
#     int test_case;
#     cin >> test_case;
#     for (int i=0; i < test_case; i++){
#         cin >> depth >> days;
#         for (int i=0; i < 1000; i++)
#             for (int j=0; j < 2000; j++)
#                 cache[i][j] = -1.0;
#         cout.precision(10);
#         printf("%.10lf\n", climb(0, 0, 1));
#     }
#     return 0;
# }

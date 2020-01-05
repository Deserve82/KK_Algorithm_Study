#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int n, m;
int minBlindSpot = 100;

int map[8][8];
int tempMap[8][8];

int dy[] = { 0, 1, 0, -1 };
int dx[] = { 1, 0, -1, 0 };

vector<pair<int, int>> cctv;

void simulate(int idx, vector<pair<int, int>> cctv, int blindSpot) {
	if (idx == cctv.size()) {
		if (minBlindSpot > blindSpot) {
			minBlindSpot = blindSpot;
		}
		return;
	}

	int original_y = cctv[idx].first;
	int original_x = cctv[idx].second;

	int cctvNo = map[original_y][original_x];

	int y, x, watchedArea;
	memcpy(tempMap, map, sizeof(map));

	if (cctvNo == 1) {
		for (int dir = 0; dir < 4; dir++) {
			watchedArea = 0;
			y = original_y;
			x = original_x;

			while (true) {
				y += dy[dir];
				x += dx[dir];
				if (y < 0 || y >= n || x < 0 || x >= m || map[y][x] == 6) {
					break;
				}
				if (map[y][x] == 0) {
					watchedArea++;
					map[y][x] = 7;
				}
			}

			simulate(idx + 1, cctv, blindSpot - watchedArea);

			if (watchedArea) {
				memcpy(map, tempMap, sizeof(map));
			}
		}
	}
	else if (cctvNo == 2) {
		for (int dir = 0; dir < 2; dir++) {
			watchedArea = 0;

			for (int coverdDir = dir, count = 0; count < 2; count++, coverdDir = (coverdDir + 2) % 4) {
				y = original_y;
				x = original_x;

				while (true) {
					y += dy[coverdDir];
					x += dx[coverdDir];
					if (y < 0 || y >= n || x < 0 || x >= m || map[y][x] == 6) {
						break;
					}
					if (map[y][x] == 0) {
						watchedArea++;
						map[y][x] = 7;
					}
				}
			}

			simulate(idx + 1, cctv, blindSpot - watchedArea);

			if (watchedArea) {
				memcpy(map, tempMap, sizeof(map));
			}

		}
	}
	else if(cctvNo == 3) {
		for (int dir = 0; dir < 4; dir++) {
			watchedArea = 0;

			for (int coverdDir = dir, count = 0; count < 2; count++, coverdDir = (coverdDir + 1) % 4) {
				y = original_y;
				x = original_x;

				while (true) {
					y += dy[coverdDir];
					x += dx[coverdDir];
					if (y < 0 || y >= n || x < 0 || x >= m || map[y][x] == 6) {
						break;
					}
					if (map[y][x] == 0) {
						watchedArea++;
						map[y][x] = 7;
					}
				}
			}

			simulate(idx + 1, cctv, blindSpot - watchedArea);

			if (watchedArea) {
				memcpy(map, tempMap, sizeof(map));
			}
		}
	}

	else if (cctvNo == 4) {
		for (int dir = 0; dir < 4; dir++) {
			watchedArea = 0;

			for (int coverdDir = dir, count = 0; count < 3; count++, coverdDir = (coverdDir + 1) % 4) {
				y = original_y;
				x = original_x;
				while (true) {
					y += dy[coverdDir];
					x += dx[coverdDir];
					if (y < 0 || y >= n || x < 0 || x >= m || map[y][x] == 6) {
						break;
					}
					if (map[y][x] == 0) {
						watchedArea++;
						map[y][x] = 7;
					}
				}
			}

			simulate(idx + 1, cctv, blindSpot - watchedArea);

			if (watchedArea) {
				memcpy(map, tempMap, sizeof(map));
			}
		}
	}
	else {
		watchedArea = 0;
		for (int coverdDir = 0, count = 0; count < 4; count++, coverdDir = (coverdDir + 1) % 4) {
			y = original_y;
			x = original_x;

			while (true) {
				y += dy[coverdDir];
				x += dx[coverdDir];
				if (y < 0 || y >= n || x < 0 || x >= m || map[y][x] == 6) {
					break;
				}
				if (map[y][x] == 0) {
					watchedArea++;
					map[y][x] = 7;
				}
			}
		}

		simulate(idx + 1, cctv, blindSpot - watchedArea);

		if (watchedArea) {
			memcpy(map, tempMap, sizeof(map));
		}
	}
	return;
}

int main() {
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	cin >> n >> m;

	int spot;
	int blindSpot = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> spot;
			if (spot == 0) {
				blindSpot++;
			}
			else if (spot == 6);
			else {
				cctv.push_back({ i, j });
			}
			map[i][j] = spot;
		}
	}
	simulate(0, cctv, blindSpot);
	cout << minBlindSpot;
}
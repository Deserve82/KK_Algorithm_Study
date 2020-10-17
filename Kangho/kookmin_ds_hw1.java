import java.util.*;

class Maze {

	private int[][] maze;	// 2 dim array for maze
	private int[][] mark;	// 2 dim array for visit marking
	private final int[][] dir = {{1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}};
	private Stack<int[]> st = new Stack<>();
	public Maze(int m, int p) {
		maze = new int[m + 2][p + 2];
		mark = new int[m + 2][p + 2];
		for(int i = 0; i < m + 2; i++)
			for(int j = 0; j < p + 2; j++) {
				maze[i][j] = 1;
				mark[i][j] = 0;
			}
	}

	// create the maze structure
	public void SetWall(int i, int j, int val) {
		maze[i][j] = val;
	}

	public void Dfs(int[] start, int m, int p) {
		st.push(start);
		if (start[0] == m && start[1] == p) {
			List<int[]> ls = new ArrayList<int[]>(st);
			for (int[] x : ls){
				System.out.println("("+x[0]+","+x[1]+")");
			}
		};
		for(int i=0; i<8; i++){
			int[] ml = {start[0]+dir[i][0], start[1]+dir[i][1]};
			if (ml[0] < 1 || ml[0] > m || ml[1] < 1 || ml[1] > p || mark[ml[0]][ml[1]] != 0 || maze[ml[0]][ml[1]] != 0) continue;
			else{
				mark[ml[0]][ml[1]] = 1;
				Dfs(ml, m, p);
				st.pop();
			}
		}
	}


	public void Path(int m, int p) {
		mark[1][1] = 1;
		Dfs(new int[]{1, 1}, m, p);
	}
}; 


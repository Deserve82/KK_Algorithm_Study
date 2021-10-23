import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int row, col;
        int answer = 1000000;
        int[][] move = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        String[] tmp = bf.readLine().split(" ");
        row = Integer.parseInt(tmp[1]);
        col = Integer.parseInt(tmp[0]);
        char[][] board = new char[row][col];
        for (int i=0; i<row; i++){
            String t = bf.readLine();
            for (int j=0; j<col; j++){
                board[i][j] = t.charAt(j);
            }
        }

        int[] start = {-1, -1};
        int[] end =  {-1, -1};
        for(int i=0; i<row; i++){
            for (int j=0; j<col; j++){
                if (board[i][j] == 'C' && start[0] == -1){
                    start[0] = i;
                    start[1] = j;
                } else if (board[i][j] == 'C' && start[0] != -1){
                    end[0] = i;
                    end[1] = j;
                }
            }
        }
        int[][] checker = new int[row][col];
        for (int i=0; i<row; i++){
            Arrays.fill(checker[i], 100000);
        }
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {start[0], start[1], 0, 0});
        q.add(new int[] {start[0], start[1], 1, 0});
        q.add(new int[] {start[0], start[1], 2, 0});
        q.add(new int[] {start[0], start[1], 3, 0});
        while (!q.isEmpty())
        {
            int[] curr = q.poll();
            int r = curr[0];
            int c = curr[1];
            int d = curr[2];
            int cost = curr[3];
            if (r == end[0] && c == end[1]){
                answer = Math.min(answer, cost);
                continue;
            }

            int mr = r + move[d][0];
            int mc = c + move[d][1];
            if (0 <= mr && mr < row && 0 <= mc && mc < col){
                if (board[mr][mc] != '*' && cost <= checker[mr][mc]){
                    checker[mr][mc] = cost;
                    for (int i=0; i<4; i++){
                        if (d == 0 || d == 2){
                            if (i == 1 || i == 3){
                                q.add(new int[] {mr, mc, i, cost +1});
                            } else {
                                if ((d == 0 && i == 2) || (d == 2 && i == 0)) continue;
                                q.add(new int[] {mr, mc, i, cost});
                            }
                          }
                        else{
                            if (i == 0 || i == 2){
                                q.add(new int[] {mr, mc, i, cost +1});
                            } else {
                                if ((d == 1 && i == 3) || (d == 3 && i == 1)) continue;
                                q.add(new int[] {mr, mc, i, cost});
                            }
                        }
                    }
                }
            }
        }
        System.out.println(checker[end[0]][end[1]]);

        bw.flush();
        bw.close();
        bf.close();
    }
}

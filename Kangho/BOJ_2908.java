import java.util.*;

class Main{
    public static void main(String [] args){
        String[] croatiaAlpha = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        int realAnswer = n.length();
        int zNumber = 0;
        for (String s : croatiaAlpha) {
            for (int i=0; i<n.length()-s.length()+1; i++){
                if (s.equals(n.substring(i,i+s.length()))){
                    if (s.equals("dz=")) zNumber += 1;
                    answer += s.length()-1;
                }
            }
        }
        System.out.println(realAnswer-answer +zNumber);
    }
}

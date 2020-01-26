using System.Linq;

public static class Kata {
    public static int TotalPoints(string[] games) {
        int answer = 0;
        
        foreach(string score in games)
        {
          int x = int.Parse(score[0].ToString());
          int y = int.Parse(score[2].ToString());
          
          if (x > y) { answer += 3; }
          else if (x == y) { answer += 1; }
        }
        return answer;
    }
}
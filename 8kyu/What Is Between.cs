using System.Collections.Generic;
public class Kata {
  public static int[] Between(int a, int b) {
    List<int> ans = new List<int>();
    for(int i = a; i <= b; i++)
    {
      ans.Add(i);
    }
    return(ans.ToArray());
  }
}
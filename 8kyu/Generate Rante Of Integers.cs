using System;
using System.Linq;
using System.Collections.Generic;
public class Kata
{
  public static int[] GenerateRange(int min, int max, int step)
  {
    List<int> ans = new List<int>();
    for(int i = min; i <= max; i += step)
    {
      ans.Add(i);
    }
    return(ans.ToArray());
  }
}
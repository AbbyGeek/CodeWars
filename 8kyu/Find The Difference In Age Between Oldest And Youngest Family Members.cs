using System;
public class Kata
{
  public static int[] DifferenceInAges(int[] ages)
  {
    Array.Sort(ages);
    int[] ans = new int[3];
    ans[0] = ages[0];
    ans[1] = ages[ages.Length-1];
    ans[2] = ans[1] - ans[0];
    return ans;
  }
}
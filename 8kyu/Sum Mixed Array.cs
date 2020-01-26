using System;
public class Kata
{
  public static int SumMix(object[] x)
  {
    int ans = 0;
    foreach( object y in x)
    {
      ans+=Convert.ToInt32(y);
    }
    return ans;
  }
}
using System;
namespace Solution
{
  public class TwiceAsOldSolution
  {
    public static int TwiceAsOld(int dadYears, int sonYears)
    {
      return(Math.Abs((sonYears*2)-dadYears));
    }
  }
}
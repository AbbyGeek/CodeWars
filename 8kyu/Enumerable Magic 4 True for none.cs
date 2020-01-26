using System;
using System.Linq;

public class Kata
{
  public static bool None(int[] arr, Func<int, bool> fun)
  {
    if (arr.Any(fun))
    {
      return false;
    }
    else
    {
    return true;
    }
  }
}
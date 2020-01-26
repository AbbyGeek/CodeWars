using System;

public class Kata
{
  public static bool All(int[] arr, Func<int, bool> fun)
  {
    foreach (int x in arr)
    {
      if(!fun(x))
      {
      return false;
      }
    
    }
    return true;
    
    
  }
}
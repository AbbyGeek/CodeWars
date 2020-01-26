using System;

public static class Kata
{
  public static string CountSheep(int n)
  {
  int sheep = 1;
  string ans = "";
    for(int i=0; i<n; i++)
    {
      ans+= (sheep + " sheep...");
      sheep++;
    }
    return ans;
  }
}
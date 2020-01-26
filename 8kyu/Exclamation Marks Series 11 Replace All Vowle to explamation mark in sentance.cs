using System;
using System.Linq;

public static class Kata
{
  public static string Replace(string s)
  {
    string vowels = "aeiouAEIOU";
    s = string.Concat(s.Select(c => vowels.Contains(c) ? '!' : c));
    return s;
  }
}
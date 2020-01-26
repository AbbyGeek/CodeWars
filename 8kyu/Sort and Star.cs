using System;

public class Kata
{
  public static string TwoSort(string[] s)
  {
    // Sory array alphabetially
    Array.Sort(s, StringComparer.Ordinal);
    
    
    // Edit first string
    string x = s[0];
    char[] y = x.ToCharArray();
    string[] z = Array.ConvertAll(y, char.ToString);
    return string.Join("***", z);
  }  
}
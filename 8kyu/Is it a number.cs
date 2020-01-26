using System;

public class CodeWars
{
  public static bool IsDigit(string s) 
  {
    float i = 0.0f;
    bool result = float.TryParse(s, out i);
    Console.WriteLine(s);
    return result;

    
  }
}
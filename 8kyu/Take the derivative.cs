using System;
public class Kata
{
  public static string Derive(double c, double e)
  {
   string x = (c*e).ToString();
   string y = (e-1).ToString();
   return x + "x^" + y;
  }
}
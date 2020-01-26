using System;

public class Kata
{
  public static string Problem(String a)
  {
  float ans;
  if(float.TryParse(a, out ans) == false)
  {
    return "Error";
  }
  else
  {
    return(float.Parse(a)*50+6).ToString();
  }
  }
}
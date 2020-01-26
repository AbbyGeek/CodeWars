public class Kata
{
  public static string Stringy(int size)
  {
    string ans = "";
    while (size > 0)
    {
      if (size >= 2)
      {
        ans += "10";
        size = size - 2;
      }
      if (size == 1)
      {
        ans += "1";
        size = size - 1;
      }

    }    
  return ans;
  }
}
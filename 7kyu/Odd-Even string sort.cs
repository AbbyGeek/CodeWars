public class Kata
{
  public static string SortMyString(string s)
  {
    int x = 0;
    string Even = "";
    string Odd = "";
    while (x < s.Length)
    {
      if (x % 2 == 0)
      {
      Even += s.Substring(x,1);
      }
      else
      {
      Odd += s.Substring(x,1);
      }
      x++;
    }
    return Even +" "+Odd;
  }
}
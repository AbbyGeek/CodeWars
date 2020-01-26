using System.Linq;
public class Kata
{
  public static string DrawStairs(int n)
  {
    int spaceNum = 1;
    string ans = "I";
    for(int i = 1; i < n; i++)
    {
      ans+="\n";
      ans += string.Concat(Enumerable.Repeat(" ", spaceNum));
      spaceNum++;
      ans += "I";
    }
    
    return(ans);
  }
}
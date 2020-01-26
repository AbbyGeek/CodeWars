using System.Linq;
using System.Collections.Generic;

public class Kata
{
  public static int[] Remove(int[] integerList, int[] valuesList)
  {
    List<int> ans = new List<int>();
    for (int i = 0; i < integerList.Length; i++)
    {
      if (valuesList.Contains(integerList[i]))
      {
        continue;
      }
      else {ans.Add(integerList[i]);}
    }
    return ans.ToArray();
  }
}
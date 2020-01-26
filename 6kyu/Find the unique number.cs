using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static int GetUnique(IEnumerable<int> numbers)
  {
    int[] unique = numbers.Distinct().ToArray();
    int count = 0;
    foreach (int x in numbers)
    {
    if (x == unique[0])
    {
    count += 1;
    }
    }
    if (count == 1){ return unique[0]; }
    else { return unique[1]; }
  }
}
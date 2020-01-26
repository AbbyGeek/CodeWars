using System.Collections.Generic;

namespace Solution
{
  class Kata
    {
    public static int find_it(int[] seq) 
      {
      Dictionary <int, int> tally = new Dictionary <int, int>();
      
      foreach (int x in seq)
      {
        if(tally.ContainsKey(x))
        {
          tally[x] += 1;
        }
        else
        {
        tally.Add(x, 1);
        }
      }
      
      foreach(KeyValuePair<int, int> key in tally)
      {
        if (key.Value % 2 != 0)
        {
          return key.Key;
        }
      }
      
      return -1;
      }
       
    }
}
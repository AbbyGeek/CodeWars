public class Kata
{
  public static int[] Maps(int[] x)
  {
    // CREATE EMPTY ANSWER ARRAY (cannot edit values in "x")
    int[] ans = new int[x.Length];
    
    // ITERATE THROUGH x MULTIPLY EACH VALUE BY 2 AND ADD TO ans
    for (int i = 0; i <x.Length; i++)
    {
      ans[i] = x[i]*2;
    }
    return ans;
  }
}
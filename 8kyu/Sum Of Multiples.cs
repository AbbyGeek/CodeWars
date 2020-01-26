public class Kata
{
  public static int SumMul(int n, int m)
  {

    int ans = 0;
    
    if (n >= m)
    {
      throw new System.ArgumentException("nope");
    }
    if (n <= 0)
    {
      throw new System.ArgumentException("nope");
    }
    else
    {
      for (int i = n; i < m+1; i = i+n)
    {
    ans += i;
    }
      return ans;
    }
  }
}
public class Kata
{
  public static bool AmIWilson(int p)
  {
  int f = 1;
  for (int i = 1; i < p; i++)
    {
        f = f * i;
    }
    f+=1;
    return(f%(p*p)==0);
  }
}
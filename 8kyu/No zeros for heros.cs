using System;

public class NoBoring 
{
    public static int NoBoringZeros(int n) 
    {
        if (n == 0)
        {
          return 0;
        }
        else
        {
          while (n % 10 == 0)
          {
            n = n/10;
          }
          return n;
        }
    }
}
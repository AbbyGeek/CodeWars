public class Kata
{
    public static int ExpressionsMatter(int a, int b, int c)
    {
        int[] arr1 = new int[] {1,2,3,4};
        arr1[0] = a*(b+c);
        arr1[1] = a*b*c;
        arr1[2] = (a+b)*c;
        arr1[3] = a+b+c;

        
        int max = 0;
        foreach (int x in arr1)
          { if (x > max)
          { max = x; }}
        
        return max;
        
    }
}
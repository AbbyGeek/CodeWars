class Kata
{
    public static string Bump(string input)
    {
      int x = 0;
      int count = 0;
      while (x < input.Length)
      {
        if (input[x].ToString() == "n")
        {
          count++;
        }
      x++;
      }
      if (count < 16)
      {
      return "Woohoo!";
      }
      else { return "Car Dead";}
    }
}
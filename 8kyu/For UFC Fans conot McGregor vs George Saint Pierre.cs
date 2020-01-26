using System;

public static class Kata
{
  public static string Quote(string fighter)
  {
    string x = fighter.ToLower();
    if (x == "george saint pierre")
      {
        return  "I am not impressed by your performance.";
      }
    else
    {
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!";
    }
  }
}
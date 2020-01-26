public static class Kata 
{
  public static bool IsLockNessMonster(string sentence) 
  {
    string lower = sentence.ToLower();
    return (lower.Contains("tree fiddy") || lower.Contains("3.50"));
  }
}
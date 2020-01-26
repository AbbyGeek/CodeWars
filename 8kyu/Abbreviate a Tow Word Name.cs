public class Kata
{
  public static string AbbrevName(string name)
  {
    string final = "";
    string[] ans = name.Split(' ');
    foreach (string x in ans)
    {
    final += x.Substring(0,1).ToUpper();
    }
    final = final.Insert(1, ".");
    return final;
  }
}
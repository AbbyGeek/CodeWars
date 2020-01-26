public class Greetings
  {
    public static string greet(string name)
      {
        if (name == "" || name == null ) {return null;}
        return($"hello {name}!");
      }
  }
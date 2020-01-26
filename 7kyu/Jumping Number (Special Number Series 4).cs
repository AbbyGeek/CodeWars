using System.Collections.Generic;
class Kata
{
    public static string JumpingNumber(int number)
    {
        List<int> intList = new List<int>();
        while (number > 0)
        {
          intList.Add(number%10);
          number = number /10;
        }
        intList.Reverse();
        
        string answer = "Jumping!!";
        for(int i=0; i < intList.Count-1; i++)
        {
          if(intList[i] != intList[i+1]-1 && intList[i] != intList[i+1]+1)
          {
            answer = "Not!!";
          }
        }
        
        return (answer);
    }
}
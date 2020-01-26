using System;

namespace CodeWars
{
    class Kata
    {
        public string driver (params string[] data)
        {
          string LastName = data[2].ToUpper();
          string Birth = data[3];
          string FirstName = data[0];
          string MidName = data[1];
          string Gender = data[4];
          
          //birth month
          string[] Months = {"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"};
          string[] MaleMonth = {"01","02","03","04","05","06","07","08","09","10","11","12"};
          string[] FemMonth = {"51","52","53","54","55","56","57","58","59","60","61","62"};
          
          int MonthNum = Array.IndexOf(Months, Birth.Substring(3,3));
          
          string Code = "";
          
          //last name
          if (LastName.Length >= 5)
          {
          Code += LastName.Substring(0,5);
          }
          else 
          {
          Code += "Blah";
          }
          
          //decade
          Code += Birth.Substring(9,1);
          
          //month w/ gender
          if (Gender == "M")
          {
          Code += MaleMonth[MonthNum];
          }
          else
          {
          Code += FemMonth[MonthNum];
          }
          
          // date within month
          Code += Birth.Substring(0,2);
          
          // Year
          Code += Birth.Substring(10,1);
          
          //First + Middle initial
          Code += FirstName.Substring(0,1);
          Code += MidName.Substring(0,1);
          
          Code += "9AA";
          return Code;
        }
    }
}
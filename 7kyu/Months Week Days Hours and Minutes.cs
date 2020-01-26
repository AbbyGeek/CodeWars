using System;

namespace Solution
{
	public class Kata
	{
		public static string DisplayValue(int test)
		{
      string Answer = "";

      int PerMonth = 60*24*7*4;
      int PerWeek = 60*24*7;
      int PerDay = 60*24;
      int PerHour = 60;
      int PerMin = 1;
      
      // MONTHS
      if (test >= PerMonth)
      {
      int Months = test / PerMonth;
        if (Months > 1)
        {
        Answer += Months.ToString() + " months ";
        }
        else
        {
        Answer += Months.ToString() + " month ";
        }
      test = test - PerMonth*Months;
      }
      
      //WEEKS
      if (test >= PerWeek)
      {
      int Weeks = test / PerWeek;
        if (Weeks > 1)
        {
        Answer += Weeks.ToString() + " weeks ";
        }
        else
        {
        Answer += Weeks.ToString() + " week ";
        }
      test = test - PerWeek*Weeks;
      }
      
      //DAYS
      if (test >= PerDay)
      {
      int Days = test / PerDay;
        if (Days > 1)
        {
        Answer += Days.ToString() + " days ";
        }
        else
        {
        Answer += Days.ToString() + " day ";
        }
      test = test - PerDay*Days;
      }
      
      //HOURS
      if (test >= PerHour)
      {
      int Hours = test / PerHour;
        if (Hours > 1)
        {
        Answer += Hours.ToString() + " hours ";
        }
        else
        {
        Answer += Hours.ToString() + " hour ";
        }
      test = test - PerHour*Hours;
      }
      
      //MINS
      if (test >= PerMin)
      {
      int Mins = test / PerMin;
        if (Mins > 1)
        {
        Answer += Mins.ToString() + " minutes ";
        }
        else
        {
        Answer += Mins.ToString() + " minute ";
        }
      test = test - PerMin*Mins;
      }
      return Answer.Substring(0,Answer.Length-1);
		}
	}
}
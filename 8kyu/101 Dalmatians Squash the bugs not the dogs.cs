public static class Kata
    {
        public static string HowManyDalmatians(int n)
        {
            string[] dogs = 
            {
                "Hardly any",
                "More than a handful!",
                "Woah that's a lot of dogs!",
                "101 DALMATIONS!!!"
            };
            if (n <= 10)
            {return dogs[0];}
            if (n <= 50)
            {return dogs[1];}
            if (n == 101)
            {return dogs[3];}
            else
            {return dogs[2];}
            
        }
    }
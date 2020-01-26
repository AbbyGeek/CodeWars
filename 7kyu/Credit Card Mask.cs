public static class Kata
{
  // return masked string
  public static string Maskify(string cc)
  {
    string answer ="";

		int ccLength = cc.Length;
			
		int i;
		for(i=0;i<ccLength; i++)
		{
			if(i < ccLength-4)	
			{
				answer += "#";
			}
			else { answer += cc[i]; }
		}
		
		return(answer);
  }
}
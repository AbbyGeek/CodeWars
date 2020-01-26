class MorseCodeDecoder
{
	public static string Decode(string morseCode)
	{  
		string[] arr = morseCode.Split(' ');
    for(int i = 0; i < arr.Length; i++)
    {
      string y = MorseCode.Get(arr[i]);
      arr[i] = y;
    }
    string ans = string.Join(" ",arr);
    ans = ans.Replace("   ", "~");
    ans = ans.Replace(" ", "");
    ans = ans.Replace("~"," ");
    ans = ans.Trim();
    return ans;
	}
}
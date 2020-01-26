using System;
public class Kata
{
  public static double SquareArea(double A)
  {
    double c = A * 4;
    double r = c / Math.PI/2;
    return Math.Round(r*r, 2);
  }
}
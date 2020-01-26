using System;
public class Kata
{
  public static double FuelPrice(double litres, double pricePerLiter)
  {
    
    if (litres >= 10)
    {
      double total = litres * (pricePerLiter - .25);
    return Math.Round(total, 2);
    }
    if (litres >= 8)
    {
      double total = litres * (pricePerLiter - .20);
    return Math.Round(total, 2);
    }
    if (litres >= 6)
    {
      double total = litres * (pricePerLiter - .15);
    return Math.Round(total, 2);
    }
    if (litres >= 4)
    {
      double total = litres * (pricePerLiter - .10);
    return Math.Round(total, 2);
    }
    if (litres >= 2)
    {
      double total = litres * (pricePerLiter - .05);
    return Math.Round(total, 2);
    }
    else
    {
    double total = litres * pricePerLiter;
    return Math.Round(total, 2);
    }
  
  
  }
  
}
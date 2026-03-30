"""Evaluate if a year is a leap year"""

def leap_year(year):
    """Calculate if a year is a leap year
    
    :param year: int - year to evalueate
    :return: boolean - indicating if is a leap year
    """

    return (year%4==0 and year%100!=0) or (year%400==0)
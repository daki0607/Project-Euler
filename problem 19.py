"""
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a
century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
"1 Jan 1901 = tues"

year = 1901
currentday = "tues"
sundays = 0
dayinmonth = {
    "Sept": 30,
    "April": 30,
    "June": 30,
    "Nov": 30,
    "Feb": 28,
    "Jan": 31,
    "March": 31,
    "May": 31,
    "July": 31,
    "Aug": 31,
    "Oct": 31,
    "Dec": 31
    }

nextday = {
    "mon": "tues",
    "tues": "wed",
    "wed": "thurs",
    "thurs": "fri",
    "fri": "sat",
    "sat": "sun",
    "sun": "mon"
    }

def leap(year):
    if (year % 4 == 0):
        dayinmonth["Feb"] = 29
        
    else:
        dayinmonth["Feb"] = 28

while (year < 2001):
    leap(year)

    
    
    year += 1















    

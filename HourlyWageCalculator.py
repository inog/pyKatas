"""
Calculate easily  yearly / monthly payment by given
given:
yearly payment, hours per week

wanted
1. pay per month
2. pay per hour

"""

yearly = 67000
hoursPerWeek = 37.5
WEEKS=52

def calcu(yearly, hoursPerWeek):
    monthly = yearly / 12
    hourly = 3 * monthly / 13 / hoursPerWeek
    print("monthly:", monthly)
    print("hourly:", hourly)

yearlyList = [60000,67000,70000,90000,100000]
weekHours = [40, 37.5, 40, 40, 42]
for y, hpw in zip(yearlyList,weekHours):
    calcu(y,hpw)
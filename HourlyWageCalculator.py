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
    return  3 * monthly / 13 / hoursPerWeek

yearlyList = [60000, 52500,67000,70000,90000,100000,100000, 110000]
weekHours = [40.0, 30.0, 37.5, 40.0, 40.0, 40.0, 42.0, 42.0]
for y, hpw in zip(yearlyList,weekHours):
    hourly = calcu(y, hpw)
    print("yearly: ", y, "hoursPerWeek: ", hpw, "monthly :", round(y/12, 2), "hourly :", round(hourly, 2) )
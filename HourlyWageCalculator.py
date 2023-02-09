"""
Calculate easily  yearly / monthly payment by given:
yearly payment, hours per week

wanted
1. pay per month
2. pay per hour

"""


def hourly_wage(yearly, week_hours):
    monthly = yearly / 12
    return 3 * monthly / 13 / week_hours


yearlyList = [65746,67000, 75000,  80000, 85000, 90000]
weekHours = [37.5, 37.5, 37.5, 40, 40, 40 ]
for y, hpw in zip(yearlyList, weekHours):
    hourly = hourly_wage(y, hpw)
    print("yearly:", y, "hoursPerWeek:", hpw, "monthly:", round(y/12, 2), "hourly:", round(hourly, 2))

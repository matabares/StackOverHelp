from datetime import datetime
import calendar


def jan_15(year,month,date):
    m1 = datetime(2020, 1, 15) - datetime(year, month, date)
    print(m1.days)

def march_25(year,month,date):
  m3=date(2020,3,25)-date(year,month,date)
  print(m3.days)


year=int(input('enter the year '))
month=int(input('enter the month: '))
date=int(input('enter the date: '))

jan_15(year,month,date)
march_25(year,month,date)
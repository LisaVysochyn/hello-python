from datetime import date

the_day = int(input())
the_month = int(input())
the_year = int(input())

date_of_birth = date(the_year, the_month, the_day)
current_date = date.today()
print((current_date-date_of_birth).days)

import datetime


y, m, d = map(int, input().split())

date = datetime.date(y, m, d)
next_d = date + datetime.timedelta(int(input()))

print(next_d.year, next_d.month, next_d.day)

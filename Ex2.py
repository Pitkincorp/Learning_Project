import datetime
now = datetime.datetime.now()
print(str(now))
get_year = lambda x: int(str(x).split()[0].split('-')[0])
get_month = lambda x: int(str(x).split()[0].split('-')[1])
get_day = lambda x: int(str(x).split()[0].split('-')[2])
print(get_year(now))
print(get_month(now))
print(get_day(now))

print(now.date())
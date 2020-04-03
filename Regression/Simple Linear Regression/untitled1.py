import datetime
curdate = datetime.datetime.now()
dateofbirth = input ('Enter your date of birth (dd/mm/yyyy) :')
dob= datetime.datetime.strptime(dateofbirth,'%d/%m/%Y')
daysleft = dob - curdate
years = -daysleft.total_seconds()/(365.242*24*3600)
months = (years-int(years))*12
days = int((months-int(months))*(365.242/12))
print('You are', int(years),'years',int(months), 'months', days,'days old')
import datetime


day		= 1
months	= range(1,13)
years 	= range(1901, 2001)

out=0
for year in years:
	for month in months:
		d=datetime.date(year,month,day).weekday()
		if d==6:
			out+=1
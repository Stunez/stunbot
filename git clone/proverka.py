from math import sin, cos, sqrt, atan2, radians

R = 6373.0

loninput = float(input())
latinput = float(input())
location = {
"lat1" : 43.235051,
'lon1' : 76.909720, #центркредит сатпаева манаса
'lat2' : 43.235210,
'lon2' : 76.908025, #tamoto
'lat3' : 43.240199,
'lon3' : 76.905399, #Сбербанк, ТЦ Глобус
'lat4' : 43.240670,
'lon4' : 76.914141 #Народный банк, Urban Athletic
}
def podchet():
		#задаем переменную для цикла
	dlon = 0
	dlat = 0
	distance2 = 9999999999
	distance = 0
	latnum = 0
	#------
	for lat,lonnum in location.items():
		
		lonnum = float(lonnum)
		
		for i in lat:
			
			if i == 'o':
				dlon = radians(loninput) - radians(lonnum)
				dlat = radians(latinput)- radians(latnum)
				a = sin(dlat / 2)**2 + cos(latnum) * cos(latinput) * sin(dlon / 2)**2
				c = 2 * atan2(sqrt(a), sqrt(1 - a))	
				distance = R * c
			elif i == 'a': 
				latnum = lonnum
		if distance == 0:
			pass
		elif distance2 > distance:
			distance2 = distance

	return distance2

#------
a = podchet()
print("Result:", a) 
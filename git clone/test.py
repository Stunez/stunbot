from math import sin, cos, sqrt, atan2, radians
info = [
	{
	'id' : 1,
	'range' : 0,
	'location' : {
			"lat1" : 43.235051,

			'lon1' : 76.909720,
		}
		},
	{
	'id' : 2,
	'range' : 0,
	"location" : 
		{
			'lat2' : 43.235210,

			'lon2' : 76.908025,
			},
	},
	
	{
	'id' : 3,
	'range' : 0,
	"location" : {
		
			'lat3' : 43.240199,

			'lon3' : 76.905399, 
			},
		},
	
	{
	'id' : 4,
	'range' : 0,
	"location" : {
		
			'lat4' : 43.240670,
	
			'lon4' : 76.914141,
			},
		},
	
	{
	'id' : 5,
	'range' : 0,
	"location" : {
		 
			'lat5' : 43.235823,

			'lon5' : 76.883344
		
		},
	},
	{
	'id' : 6,
	'range' : 0,
	"location" : {
		 
			'lat5' : 43.235804,

			'lon5' : 76.883513
		
		},
	},
]


R = 6373.0

latinput = float(input())
loninput = float(input())

dlon = 0
dlat = 0
distance2 = 9999999999
distance = 0
latnum = 0
for lat in info:
	for x in lat['location']:
		#print (lat['location'][x])
		lat['location'][x] = float(lat['location'][x])
		for y in x:
			if y == 'o':
				dlon = radians(loninput) - radians(lat['location'][x])
				dlat = radians(latinput)- radians(latnum)
				a = sin(dlat / 2)**2 + cos(latnum) * cos(latinput) * sin(dlon / 2)**2
				c = 2 * atan2(sqrt(a), sqrt(1 - a))	
				distance = R * c
			elif y == 'a': 
				latnum = lat['location'][x]
				
		if distance == 0:
			pass
		elif distance2 > distance:
			distance2 = distance

	lat['range'] = distance
	print (lat['range'])

print (info)
"""
def podchet():
		#задаем переменную для цикла
	dlon = 0
	dlat = 0
	distance2 = 9999999999
	distance = 0
	latnum = 0
	lon[i] = 0
	#------
	for lat in info['restoran']:
		
		lonnum['location'] = float(lonnum['location'])
		
		for i in lat['location']:
			
			if i == 'o':
				dlon = radians(loninput) - radians(lonnum['location'])
				dlat = radians(latinput)- radians(latnum['location'])
				a = sin(dlat / 2)**2 + cos(latnum['location']) * cos(latinput) * sin(dlon / 2)**2
				c = 2 * atan2(sqrt(a), sqrt(1 - a))	
				distance = R * c
			elif i == 'a': 
				latnum['location'] = lonnum['location']
		if distance == 0:
			pass
		elif distance2 > distance:
			distance2 = distance

	return distance2

a = podchet()
print("Result:", a) 

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(43.235051)
lon1 = radians(76.909720)
lat2 = radians(43.235210)
lon2 = radians(76.908025)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
"""
"""
MAI
"""
#making lists + dictionaries for subway lines

line_1 = {
	'Finch': 1, 'North York Centre': 2, 'Sheppard-Yonge': 3, 
	'York Mills': 4,'Lawrence': 5, 'Eglinton': 6, 'Davisville': 7, 
	'St. Clair': 8,'Summerhill': 9, 'Rosedale': 10, 'Bloor-Yonge': 11,
	'Wellesley': 12, 'College': 13, 'Dundas': 14, 'Queen': 15,
	'King': 16, 'Union': 17, 'St. Andrew': 18, 'Osgoode': 19,
	'St. Patrick': 20, 'Queens Park': 21, 'Museum': 22, 'St. George': 23,
	'Spadina': 24, 'Dupont': 25, 'St. Clair West': 26, 'Eglinton West': 27,
	'Glencairn': 28, 'Lawrence West': 29, 'Yorkdale': 30, 'Wilson': 31,
	'Sheppard West': 32, 'Downsview Park': 33, 'Finch West': 34,
	'York University': 35, 'Pioneer Village': 36, 'Highway 407': 37,
	'Vaughan Metropolitan Centre': 38
}

line_2 = {'Kennedy':1, 'Warden':2, 'Victoria Park':3, 'Main Street':4,
      	'Woodbine': 5, 'Coxwell':6, 'Greenwood': 7, 'Donlands': 8,
      	'Pape': 9, 'Chester': 10, 'Broadview': 11, 'Castle Frank': 12,
      	'Sherbourne': 13, 'Bloor-Yonge': 14, 'Bay': 15, 'St. George': 16,
      	'Spadina': 17, 'Bathurst': 18, 'Christie': 19, 'Ossington': 20,
      	'Dufferin': 21, 'Lansdowne': 22, 'Dundas West': 23, 'Keele': 24,
      	'High Park': 25, 'Runnymede': 26, 'Jane': 27, 'Old Mill': 28,
      	'Royal York': 29, 'Islington': 30, 'Kipling': 31}

line_3 = {
	'McCowan': 1, 'Scarborough Centre': 2, 'Midland': 3,'Ellesmere': 4,
	'Lawrence East': 5, 'Kennedy': 6
}

line_4 = {
	'Don Mills': 1, 'Leslie': 2, 'Bessarion': 3, 'Bayview': 4,
	'Sheppard Yonge': 5
}

lines = [line_1, line_2, line_3, line_4]

#print("the station is:", line_1['Finch'] )
statement = "Take an Uber. In this case, TTC stands for "
statement += "Take The Cab"





"""
IZZY
Find route between start_station and end_station.
"""

transfer_stations = [
	"St.George",
	"Spadina",
	"Bloor-Yonge",
	"Kennedy",
	"Sheppard-Yonge"
	]

def line_in_common(start, end_line, transfer_stations_list):
	"""
	find whether the start and end stations have a line in common, 
	assuming one or more is a transfer station
	"""
	if start in transfer_stations:
		if start in end_line:
			return end_line

def find_start_line(start, lines_list):
	"""
	find the line the start station is on
	"""
	for line in lines:
		for station in line:	
			if station == start:
				return line    
    
def find_end_line(end, lines_list):
	"""
	find the line the end station is on
	"""
	for line in lines:
		for station in line:
			if station == end:
				return line
       	 
def station_in_common(start_station, start_line, end_line):
	"""
	find if the lines have a transfer station in common
	and return the common station that is closest to the start station
	"""
	stations_start_line = set(start_line.keys())
	stations_end_line = set(end_line.keys())
	intersection = stations_start_line & stations_end_line
	transfer_value = 100
	for station in intersection:
		if abs(start_line[start_station] - start_line[station]) \
		   < transfer_value:
			return station

def closest_transfer(input_station, input_line):
	"""
	find transfer station closest to input station, which is on the way to
	the end_line
	"""
	line = list(input_line.keys())
	closest_value = 100
	closest_transfer = None
	for station in transfer_stations:
		if station in line and station != input_station:
			current_value = abs(input_line[station] - input_line[input_station])
			if current_value < closest_value:
				current_value = closest_value
				closest_transfer = station
	return closest_transfer  

def find_transfer_line(transfer_station, input_line, lines_list):
	"""
	for the input transfer station, find and return the line that is not
	the input line
	"""
	for line in lines_list:
		if transfer_station in line.keys():
			if line != input_line:
				transfer_line = line
				return transfer_line   

def find_route(start_station, end_station):
	"""
	Find route and give directions to the user
	"""
	start_line = find_start_line(start_station, lines)
	#set start_value to value of start_station
	start_value = start_line[start_station]
	if start_line == find_end_line(end_station, lines):
		#set end_value to value of end_station
		end_value = start_line[end_station]		
		#subtract start_value from end_value, make this number abs
		path_1 = abs(start_value - end_value)
		#print statement that says the number of stations on user's route
		if path_1 == 1:
			route = "Your route is 1 station from "
			route += start_station + " to " + end_station
			print(route)       	 
		else:   
			route = "Your route is " + str(path_1) + " stations from "
			route += start_station + " to " + end_station
			print(route)
	else:
		#if end_station is not on the same line as start_station:
		#if end_station line and start_station line have a station in 
		#common:
		end_line = find_end_line(end, lines)
		end_value = end_line[end_station]
		transfer = station_in_common(start_station, start_line, end_line)
		if transfer != None:
			#set start_value to value of start_station
			start_value = start_line[start_station]       	 
			#set transfer_value to value of transfer_station
			transfer_value = start_line[transfer]
			#subtract start_value from transfer_value, make this number abs
			#store that value as path_1
			path_1 = abs(transfer_value - start_value)
			#subtract end_value from transfer_value, make this number abs
			#change transfer value to end line transfer value
			transfer_value = end_line[transfer]
			#store that value as path_2           	 
			path_2 = abs(transfer_value - end_value)
			#print directions, telling user how many stations they'll pass through
			#on each line, and what their transfer station is
			route = "Your route is " + str(path_1) + " stations from "
			route += start_station + " to your transfer station "
			route += transfer + " and " + str(path_2)
			route += " stations from " + transfer
			route += " to " + end_station
			print(route)
		 
		else:
			print(statement)
			 
           	 

sentence = "Disclaimer: This program is intended to replicate the psychologically "
sentence += "damaging experience of taking the TTC. \nAny and all bugs are "
sentence += "intentional and true to life. \nUser discretion is advised. \nEnjoy the ride. "
sentence += "\nAre there any TTC routes you'd like me to find? "
sentence += "\nType 'NO' to end program or enter to continue: "
answer = input(sentence)
while answer != "NO":
	"""
	JRUE
	"""
	#asking users for input on where are they came from and where are they going"
	start = input("Where is your starting point? ")
	start = start.title()
	#checking if input is in subway stations

	"""MAI"""
	if start in line_1 or line_2 or line_3 or line_4:
		print(start)
	else:
		print("Must be a TTC subway station")
    
	end = input("Where is your end point? ")
	end = end.title()
	
	if  end in line_1 or line_2 or line_3 or line_4:
		print(end)
		print("You are going from " + start + " to " + end)
		find_route(start, end)
		break
	else:
		print("Must be a TTC subway station")
    
    
print("Thank you for riding the rocket!")
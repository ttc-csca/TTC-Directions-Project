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
	'Sheppard-Yonge': 5
}

lines = [line_1, line_2, line_3, line_4]

#print("the station is:", line_1['Finch'] )





"""
IZZY
Find route between start_station and end_station.
"""

transfer_stations = [
	"St. George",
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
		if (station in line) and (station != input_station):
			current_value = abs(input_line[station] - input_line[input_station])
			if current_value < closest_value:
				closest_value = current_value
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
			#if end_station and start_station don't intersect
			#and stations_in_common returns None:
			#select the transfer station that has the lowest value difference
			#when subtracted from input location
			#set that station to transfer_1
			transfer_1 = closest_transfer(start_station, start_line)
			#set transfer_1 value to transfer_1_value:
			transfer_1_value = start_line[transfer_1]
			#subtract start_value from transfer_1_value and make abs
			#set this value to path_1
			path_1 = abs(transfer_1_value - start_value)
			#set other line of transfer station to tl_1
			tl_1 = find_transfer_line(transfer_1, start_line, lines)
			#set transfer_1_value to its value on the transfer line
			transfer_1_value = tl_1[transfer_1]
			#set transfer_station_2 to station at intersection between
			#currently in use line and ending line
			transfer_2 = station_in_common(transfer_1, tl_1, end_line)
		 
			if transfer_2 != None:
				#if there's a transfer station
				#in common with the end line
				#set transfer_2_value to value of transfer_2
				transfer_2_value = tl_1[transfer_2]
				#subtract transfer_1_value from transfer_2_value and make value abs
				#set this value to path_2
				path_2 = abs(transfer_1_value - transfer_2_value)
				#set transfer_2_value to its value on the end line
				transfer_2_value = end_line[transfer_2]
				#subtract transfer_2_value from end_value and make value abs
				#set this value to path_3
				path_3 = abs(transfer_2_value - end_value)
				#print directions, telling user how many stations they'll pass through
				#on each line, and what their transfer stations are.
				route = "Your route is " + str(path_1) + " stations from "
				route += start_station + " to your first transfer station "
				route += transfer_1 + " \nIt's then " + str(path_2)
				route += " stations from " + transfer_1
				route += " to your second transfer: " + transfer_2
				route += "\n" + transfer_2 + " is then " + str(path_3)
				route += " stations from " + end_station + ", your final stop."
				print(route)
			else:
				#if end_line and tl_1 don't have a station in common:
				#select the transfer station that has the lowest difference for the
				#line that start_station is on
				#set that station to transfer_2 and its value to transfer_2_value
				transfer_2 = closest_transfer(transfer_1, tl_1)
				transfer_2_value = tl_1[transfer_2]
				#subtract transfer_2_value from transfer_1_value and make it abs
				#set that value to path_2
				path_2 = abs(transfer_1_value - transfer_2_value)
				#set other line of transfer_2 to tl_2
				tl_2 = find_transfer_line(transfer_2, tl_1, lines)
				#set transfer_3 to the intersection of the currently in use line
				#and the ending line
				#set transfer_3_value to value of transfer_3
				transfer_3 = station_in_common(transfer_2, tl_2, end_line)
				transfer_3_value = tl_2[transfer_3]
				#subtract transfer_value_3 from transfer_value_2 and make it abs
				#set value to path_3
				path_3 = abs(transfer_2_value - transfer_3_value)
				#set transfer_3_value to the station's value on its other line
				transfer_3_value = end_line[transfer_3]
				#subtract transfer_value_3 from end_value and make it abs
				#set value to path_4
				path_4 = abs(transfer_3_value - end_value)
				#print directions, telling user how many stations they'll pass through
				#on each line, and what their transfer station is
				statement = "\nYou should"
				statement += "take an Uber. In this case, "
				statement += "TTC stands for 'Take The Cab'"
				statement += "\n\nBut if you're really that "
				statement += "desperate, the directions are below: "
				print(statement)
				route = "\n\nYour route is " + str(path_1) + " stations from "
				route += start_station + " to your first transfer station "
				route += transfer_1 + "\n" + transfer_1
				route += " is then " + str(path_2) + " stations from " 
				route += transfer_1 + " to your second transfer: "
				route += transfer_2 + "\n" + transfer_2 + " is then "
				route += str(path_3) + " stations from "
				route += transfer_3 + " your last transfer "
				route += transfer_3 + "\n" + transfer_3 + " is then " 
				route += str(path_4) + " stations from "
				route += end_station + ", your final destination..."
				print(route)   	 
			 
           	 
sentence = "\n** Disclaimer: This program is intended to replicate the psychologically "
sentence += "damaging experience of taking the TTC. \nAny and all bugs are "
sentence += "intentional and true to life. \nUser discretion is advised..."
sentence += "\nEnjoy the ride! **"
sentence += "\n\nAre there any TTC routes you'd like me to find? "
sentence += "\nType 'NO' to end program, or any other key to continue: "
answer = input(sentence)

while answer != "NO":
	#asking users for input on where are they came from and where are they going"
	start = input("Where is your starting point? ")
	start = start.title()
	#checking if input is in subway stations
	if (start in line_1) or (start in line_2) or (start in line_3)\
	or (start in line_4):
		print(start)
		break
	else:
		print("Answer must be a TTC subway station")
		
while answer != "NO":
	end = input("Where is your end point? ")
	end = end.title()
	if (end in line_1) or (end in line_2) or (end in line_3)\
	or (end in line_4):
		print(start)
		print("\nYou are going from " + start + " to " + end)
		find_route(start, end)
		break
	else:
		print("Answer must be a TTC subway station")
		print("Please reenter your route: ")
    
    
print("Thank you for riding the rocket!")

import sys
import getopt
import json
import os.path
from pprint import pprint

def usage():
	print("sensor.py [OPTION]... [CONFIG FILE]")
	print("")

	print("\t-h,--help\t\tShow usage")
	
	print("\t-f,--frequency=FLOAT\tSet sensor frequency")
	print("\t-m,--monitor-ip=IP\tSet monitor IP address")
	print("\t-n,--hostname=STRING\tSet host name")
	print("\t-s,--sensorname=STRING\tSet sensor name")
	print("\t-u,--username=STRING\tSet username")
	print("\t-p,--password=STRING\tSet password")

	
def load(filename):
	if not os.path.isfile(filename):
		print("File doesn't exists \"" + filename + "\"");
		return [0,"","","","",""]
		
	jsonData=open(filename)
	data = json.load(jsonData)
	#pprint(data)
	jsonData.close()
	
	return [ data["frequency"], data["monitor-ip"], data["hostname"], data["sensorname"], data["username"], data["password"] ]
	

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hf:m:n:s:u:p:", ["help", "frequency=","monitor-ip=","hostname=","sensorname=","username=","password="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
		
	# Check if filename is given when no options
	if len(args) == 0 and len(opts) == 0:
		usage()
		sys.exit()
		
	frequency = 0
	monitorIP = ""
	hostname = ""
	sensorname = ""
	username = ""
	password = ""
	
	# Load config file
	if len(args) == 1:
		frequency,monitorIP,hostname,sensorname,username,password = load(args[0])
		
	# Parse options
	for o,value in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-f", "--frequency"):
			try:
				float(value)
			except ValueError:
				print("Frequency must be positive float")
				sys.exit(2)
		
			if float(value) <= 0:
				print("Frequency must be positive float")
				sys.exit(2)
				
			frequency = float(value)
			
		elif o in ("-m", "--monitor-ip"):
			monitorIP = value
		elif o in ("-n", "--hostname"):
			hostname = value
		elif o in ("-s", "--sensorname"):
			sensorname = value
		elif o in ("-u", "--username"):
			username = value
		elif o in ("-p", "--password"):
			password = value
		else:	
			print("Unhandled option")
			sys.exit(2)	

if __name__ == "__main__":
	main(sys.argv[1:])
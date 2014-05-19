import sys
import getopt
import json
import os.path
import socket
from pprint import pprint

def usage():
	print("sensor.py [OPTION]... [CONFIG FILE]")
	print("")

	print("\t-h,--help\t\tShow usage")
	
	print("\t-f,--frequency=FLOAT\tSet sensor frequency")
	print("\t-m,--monitor-ip=IP\tSet monitor IP address")
	print("\t-d,--port=INT\t\tSet UDP port")
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
	
	try:
		result = [ data["frequency"], data["monitor-ip"], data["port"], data["hostname"], data["sensorname"], data["username"], data["password"] ]
	except KeyError as err:
		print ("No key " + str(err) + "in config file")
		sys.exit(2)
		
	return result
	

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hf:m:d:n:s:u:p:", ["help", "frequency=","monitor-ip=","port=","hostname=","sensorname=","username=","password="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
		
	# Check if filename is given when no options
	if len(args) == 0 and len(opts) == 0:
		usage()
		sys.exit()
		
	frequency = 0
	monitorIP = "127.0.0.7"
	port = 0
	hostname = ""
	sensorname = ""
	username = ""
	password = ""
	
	# Load config file
	if len(args) == 1:
		frequency,monitorIP,port,hostname,sensorname,username,password = load(args[0])
		
	# Parse options
	for o,value in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-f", "--frequency"):
			frequency = value
		elif o in ("-m", "--monitor-ip"):
			monitorIP = value
		elif o in ("-d", "--port"):
			port = value
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
			
	# Frequency validation
	
	try:
		float(frequency)
	except ValueError:
		print("Frequency must be positive float")
		sys.exit(2)

	if float(frequency) <= 0:
		print("Frequency must be positive float")
		sys.exit(2)
		
	frequency = float(frequency)
	
	# Port validation
	
	try:
		int(port)
	except ValueError:
		print("Port must be positive integer")
		sys.exit(2)

	if float(frequency) <= 0:
		print("Port must be positive integer")
		sys.exit(2)
		
	port = int(port)
	
	# Monitor IP validation
	
	try:
		socket.inet_aton(monitorIP)
	except socket.error:
		print("Invalid monitor IP")
		sys.exit(2)
		

if __name__ == "__main__":
	main(sys.argv[1:])
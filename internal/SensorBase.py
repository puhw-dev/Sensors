from internal.Options import *
import socket
import threading

class SensorBase:

	"Base class for all sensors"

	interval = 0.0
	sock = None
	IP = ""
	port = 0
	encoding = 'UTF-8'

	def __init__(self, options):
		self.options = options
		self.interval = 1.0/options.frequency
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.IP = options.monitorIP
		self.port = options.port

	# Main method - runs sensor logic

	def run(self):
		print("====================================")
		print("Hello, World!")
		print("My name is " + self.getSensorName())
		print("====================================")
		self.register()
		self.sendMetrics()

	# Register sensor in monitor.
	# If fail just exit

	def register(self):
		msg = bytes("register_me", self.encoding)
		self.sock.sendto(msg, (self.IP, self.port))
		print("Sensor registered")
		

	def sendMetrics(self):
		print("Sending metrics...")
		threading.Timer(self.interval, self.sendMetrics).start()


	# Wrapper for sensor name
	def getSensorName(self):
		return self.options.sensorname;

	# Wrapper for host name
	def getHostName(self):
		return self.options.hostname;

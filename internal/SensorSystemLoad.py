import os
import psutil 
from internal.SensorBase import *

class SensorSystemLoad(SensorBase):

	"Provides information about system load"
	def __init__(self, options):
		SensorBase.__init__(self,options)

	# Return free memory in bytes
	def freeMemory(self):
		return psutil.virtual_memory().free
		
	# Return system-wide CPU utilization as float
	def cpuUtilization(self):
		return psutil.cpu_percent(0.2)

	def work(self):

		while True:
			print("Sending metrics for SystemLoad...")
			sleep(self.interval)



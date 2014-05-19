import os
import psutil 

class SystemLoad:

	"Provides information about system load"
	
	# Return free memory in bytes
	@staticmethod
	def freeMemory():
		return psutil.virtual_memory().free
		
	# Return system-wide CPU utilization as float
	@staticmethod
	def cpuUtilization():
		return psutil.cpu_percent(interval=0.2)
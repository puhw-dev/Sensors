import os
import platform
import psutil 
import socket

class SystemInfo:

	"Provides general information about system"
	
	# Return system name f.e. 'Windows 7'
	@staticmethod
	def name():
		return platform.system() + " " + platform.release()
		
	# Return my IP
	# Doesn't work with hostnames where are polish characters 
	@staticmethod
	def IP():
		return socket.gethostbyname(socket.gethostname())

	# Return hostname
	@staticmethod
	def hostname():
		return socket.gethostname()
		
	# Return CPU name
	@staticmethod
	def CPU(): 
		return platform.processor()
		
	# Return architecture (32bit, 64bit)
	@staticmethod
	def architecture():
		return platform.architecture()[0]

	# Return total amount of installed RAM in bytes.
	@staticmethod
	def totalRAM():
		mem = psutil.virtual_memory()
		return int(mem.total)
		
	# Return total size of disks in bytes.
	@staticmethod
	def totalDiskSpace():
		return psutil.disk_usage('/').total
import psutil 

class NetworkInfo:

	"Provides information about network"
	
	# Return bytes send
	@staticmethod
	def bytesSent():
		return psutil.net_io_counters().bytes_sent
		
	# Return bytes received
	@staticmethod
	def bytesReceived():
		return psutil.net_io_counters().bytes_recv
		
	# Return packets sent
	@staticmethod
	def packetsSent():
		return psutil.net_io_counters().packets_sent
		
	# Return packets received
	@staticmethod
	def packetsReceived():
		return psutil.net_io_counters().packets_recv
from internal.SystemInfo import *
from internal.SystemLoad import *
from internal.NetworkInfo import *

print("========= SystemInfo =========")
print("System name:\t\t%s" % SystemInfo.name())
print("Architecture:\t\t%s" % SystemInfo.architecture())
print("Hostname:\t\t%s" % SystemInfo.hostname())
print("CPU name:\t\t%s" % SystemInfo.CPU())
print("Total RAM:\t\t%f GB" % (SystemInfo.totalRAM() / 1024.0 / 1024.0 / 1024.0) )
print("Total disk space:\t%f GB" % (SystemInfo.totalDiskSpace() / 1024.0 / 1024.0 / 1024.0) )
#print("Host IP:\t\t%s" % SystemInfo.IP())
print("")
print("========= SystemLoad =========")
print("Free memory:\t\t%f MB" % (SystemLoad.freeMemory() / 1024.0 / 1024.0) )
print("CPU utilization:\t%0.2f%%" % SystemLoad.cpuUtilization())

print("")
print("======== NetworkInfo =========")
print("Bytes sent:\t\t%d" % NetworkInfo.bytesSent() )
print("Bytes recv:\t\t%d" % NetworkInfo.bytesReceived() )
print("Packets sent:\t\t%d" % NetworkInfo.packetsSent() )
print("Packets recv:\t\t%d" % NetworkInfo.packetsReceived() )

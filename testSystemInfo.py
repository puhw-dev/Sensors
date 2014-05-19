from internal.SystemInfo import *

print("System name:\t\t%s" % SystemInfo.name())
print("Architecture:\t\t%s" % SystemInfo.architecture())
print("Hostname:\t\t%s" % SystemInfo.hostname())
print("CPU name:\t\t%s" % SystemInfo.CPU())
print("Total RAM:\t\t%f GB" % (SystemInfo.totalRAM() / 1024.0 / 1024.0 / 1024.0) )
print("Total disk space:\t%f GB" % (SystemInfo.totalDiskSpace() / 1024.0 / 1024.0 / 1024.0) )
#print("Host IP:\t\t%s" % SystemInfo.IP())

import psutil
import matplotlib as pst
%matplotlib inline 

# Authors: ccm7676 , itay-cyber


class CPUMonitor():
    def __init__(self):
        pass
    
    def getCpuPerc(self, interval):
        return psutil.cpu_percent(interval=interval)

    def getMem(self):
        pass



cpuMon = CPUMonitor()

intervalMon = input("Interval for calculating cpu percentage: ")

print("CPU Percent: " + str(cpuMon.getCpuPerc(10)))


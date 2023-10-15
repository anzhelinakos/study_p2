import psutil
import datetime
from decor import log
from decor import speed_info

@log("record_info.txt")
def get_cputime_info():
    return {"user": psutil.cpu_times().user,
            "nice": psutil.cpu_times().nice,
            "system": psutil.cpu_times().system,
            "idle": psutil.cpu_times().idle}


@log("record_info.txt")
@speed_info
def get_cpupercent_info():
    return psutil.cpu_percent()


@log("record_info.txt")
@speed_info
def get_cpucount_info():
    return psutil.cpu_count()


@log("record_info.txt")
def get_cpufreq_info():
    return psutil.cpu_freq()


@log("record_info.txt")
def get_virtualmemory_info():
    return psutil.virtual_memory()


def get_netiocounters_info():
    return psutil.net_io_counters()

